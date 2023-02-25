from typing import Union

import yaml

from mypydantic.helpers.logger import CustomLogger
from mypydantic.helpers.parsers import sanitize
from mypydantic.models.web_acl import WebACL

LOG = CustomLogger()
LOG.local = True


def get_object(example: str) -> Union[WebACL, None]:
    object_map = {"web_acl": WebACL}
    return object_map[example]


def get_config(example: str) -> dict:
    with open(f"mypydantic/{example}.yaml", "r") as read_file:
        return sanitize(yaml.safe_load(read_file))


def main(example: str) -> Union[WebACL, None]:
    resource_config = get_config(example)
    resource_object = get_object(example)
    return resource_object(**resource_config)


if __name__ == "__main__":
    example = "web_acl"
    response = main(example)
    LOG.info(response)
    LOG.info(response.name)
    LOG.info(response.rules)
    LOG.info(response.create_object())
