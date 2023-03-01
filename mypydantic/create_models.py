# pylint: disable=protected-access,line-too-long
import importlib
import os
import re
from datetime import datetime
from typing import Dict, Literal, Optional

import jinja2
from mypy_boto3 import submodules
from mypy_boto3_wafv2 import type_defs

from mypydantic.constants import (
    BASEMODEL_NAME_CONFLICTS,
    SUPPORTED_SERVICES,
    TEMPLATE_DIR,
    TYPE_CASTS,
)
from mypydantic.helpers.logger import CustomLogger
from mypydantic.helpers.parsers import snake_case

LOG = CustomLogger()
LOG.local = True


def generate_model_file(
    service: str, model: str, is_test: Optional[bool] = False
) -> None:
    base_model_path = f"{os.getcwd()}/mypydantic/models/"
    model_path = (
        base_model_path + f"{service}.py"
        if not is_test
        else base_model_path + f"{service}_test.py"
    )
    template = get_base_template()
    file_content = template.render(current_date=datetime.now().ctime(), model=model)
    with open(model_path, "w", encoding="utf-8") as write_file:
        write_file.write(file_content)
    LOG.info(f"Model Generated: {service}")


def get_base_template() -> jinja2.Template:
    template_loader = jinja2.FileSystemLoader(TEMPLATE_DIR)
    template_env = jinja2.Environment(loader=template_loader)
    config_template = "base.jinja"
    return template_env.get_template(config_template)


def check_attributes(
    object: object,
) -> Dict[
    Literal[
        "has_name",
        "has_annotations",
        "has_origin",
        "has_origin_name",
        "has_forward_arg",
    ],
    bool,
]:
    return {
        "has_name": hasattr(object, "__name__"),
        "has_annotations": hasattr(object, "__annotations__"),
        "has_origin": hasattr(object, "__origin__"),
        "has_origin_name": hasattr(object, "_name"),
        "has_forward_arg": hasattr(object, "__forward_arg__"),
    }


def get_type(model_type: object):
    attributes = check_attributes(model_type)
    if attributes["has_name"]:
        return model_type.__name__
    if attributes["has_annotations"]:
        return get_type(model_type.__annotations__)
    if attributes["has_origin"]:
        try:
            model_name = model_type._name
            if model_name is None:
                model_attributes = check_attributes(model_type)
                if model_attributes["has_origin"]:
                    origin_attributes = check_attributes(model_type.__origin__)
                    if origin_attributes["has_origin_name"]:
                        model_name = model_type.__origin__._name
                    else:
                        model_name = model_type.__origin__.__name__
            arg_list = []
            args = model_type.__args__
            for arg in args:
                arg_type = get_type(arg)
                arg_list.append(arg_type)
            arg_string = str(arg_list).replace("'", "")
            return f"{model_name}{arg_string}"
        except:
            LOG.info(model_type.__dict__)
            raise
    if attributes["has_origin_name"]:
        return f"{model_type._name}"
    if attributes["has_forward_arg"]:
        return f"{model_type.__forward_arg__}"
    return f'"{model_type}"'


def build_model_properties(
    build_model_template: str,
    annotations: dict,
    opitonal_args: list,
) -> str:
    for model_property, model_type in annotations.items():
        property_type = get_type(model_type)
        for type_cast in TYPE_CASTS:
            pattern = rf"(\b{type_cast}\b)((?:\[[^\]]*\])?)"
            replacement = r"Type[\g<1>\g<2>]"
            property_type = re.sub(pattern, replacement, property_type)
        is_optional = False
        model_alias = model_property
        if str(model_property) in opitonal_args:
            is_optional = True
        if str(model_property).lower() in BASEMODEL_NAME_CONFLICTS:
            model_property = f"{snake_case(str(model_property))}_"
        else:
            model_property = f"{snake_case(str(model_property))}"
        if is_optional:
            property_model = f'\t{model_property}: Optional[{property_type}] = Field(default=None,alias="{model_alias}")\n'
        else:
            property_model = (
                f'\t{model_property}: {property_type} = Field(alias="{model_alias}")\n'
            )
        build_model_template += property_model
    return build_model_template


def build_model(service: str, type_defs: type_defs):
    LOG.info(f"Building Models for: {service}")
    build_model_template = "\n"
    for type_def in type_defs.__all__:
        # if str(type_def) == "CreateWebACLRequestRequestTypeDef":
        type_def_model = getattr(type_defs, type_def)
        annotations = type_def_model.__annotations__
        opitonal_args = list(getattr(type_def_model, "__optional_keys__"))
        build_model_template += f"\nclass {type_def_model.__name__}(BaseModel):\n"
        build_model_template = build_model_properties(
            build_model_template, annotations, opitonal_args
        )
    model = build_model_template.replace("TypeDef", "").replace(
        "RequestRequest", "Request"
    )
    LOG.debug(model)
    generate_model_file(service, model, is_test=False)


def main():
    for sub in submodules.SUBMODULES:
        service = sub.import_name.rstrip("_")
        if service in SUPPORTED_SERVICES:
            module = importlib.import_module(sub.module_name)
            type_defs = getattr(module, "type_defs")
            build_model(service, type_defs)


if __name__ == "__main__":
    main()
