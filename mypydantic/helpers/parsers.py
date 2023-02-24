from typing import Literal


def snake_case(text: str):
    convert = "".join(["_" + i.lower() if i.isupper() else i for i in text]).lstrip("_")
    check_convert = convert.split("_")
    # Handle ARN, IP, HTTP, AWS, KMS
    return "".join(
        [
            "" + j if len(j) == 1 and j not in ("p", "s") else j + "_"
            for j in check_convert
        ]
    ).rstrip("_")


def camel_case(text: str):
    # AWS uses ARN, IP, KMS, AWS, etc...
    return "".join(
        [
            i.capitalize() if i not in ("arn", "ip", "aws", "kms") else i.upper()
            for i in text.split("_")
        ]
    )


def convert_all_keys(dict_object: dict, conversion_type: Literal["snake", "camel"]):
    if conversion_type == "snake":
        case_type = snake_case
    if conversion_type == "camel":
        case_type = camel_case
    case_keys = [case_type(i) for i in dict_object.keys()]
    message = dict(zip(case_keys, list(dict_object.values())))
    for key, value in dict_object.items():
        if isinstance(value, dict):
            message[case_type(key)] = convert_all_keys(value, conversion_type)
        if isinstance(value, list):
            for idx, item in enumerate(value):
                if isinstance(item, dict):
                    message[case_type(key)][idx] = convert_all_keys(
                        item, conversion_type
                    )
    return message


def sanitize(dict_object: dict) -> dict:
    for key, value in dict_object.items():
        if isinstance(value, str):
            dict_object[key] = value.replace("\n", " ").rstrip(" ")
        if isinstance(value, dict):
            sanitize(value)
        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    sanitize(item)
    return dict_object
