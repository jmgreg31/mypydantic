import json

from mypydantic.helpers.logger import CustomLogger
from mypydantic.helpers.parsers import convert_all_keys

LOG = CustomLogger()
LOG.local = True


def create():
    with open("templates/web_acl.json", "r", encoding="utf-8") as read_file:
        base_json = json.loads(read_file.read())
        snake_json = convert_all_keys(base_json, "snake")
        LOG.info(snake_json)

    with open("templates/web_acl_snake.json", "w", encoding="utf-8") as write_file:
        write_file.write(json.dumps(snake_json, indent=4))


if __name__ == "__main__":
    create()
