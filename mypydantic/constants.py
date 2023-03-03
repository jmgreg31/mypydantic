import os

TEMPLATE_DIR = f"{os.getcwd()}/mypydantic/templates"
BASEMODEL_NAME_CONFLICTS = [
    "json",
    "none",
    "global",
    "from",
    "and",
    "lambda",
    "else",
    "or",
    "not",
    "return",
    "schema",
]
TYPE_CASTS = ["IO", "StreamingBody"]
