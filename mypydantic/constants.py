import os

TEMPLATE_DIR = f"{os.getcwd()}/mypydantic/templates"
BASEMODEL_NAME_CONFLICTS = ["json", "none"]
TYPE_CASTS = ["IO", "StreamingBody"]
SUPPORTED_SERVICES = ["wafv2", "lambda", "cloudformation"]
