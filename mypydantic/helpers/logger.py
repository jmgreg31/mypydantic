# pylint: disable = super-with-arguments,broad-exception-caught
import decimal
import json
import logging
import os
from datetime import datetime
from typing import Optional, Union

import coloredlogs


class JsonHelper(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return int(o)
        if isinstance(o, set):
            return list(o)
        if isinstance(o, bytes):
            return str(o)
        if isinstance(o, datetime):
            return str(o)
        return super(JsonHelper, self).default(o)


class CustomLogger:
    log_level = os.getenv("LOG_LEVEL", "INFO")
    local = False
    propogate = False

    def log(self):
        logger = logging.getLogger(__name__)
        logger.handlers = []
        if self.log_level == "ERROR":
            coloredlogs.DEFAULT_FIELD_STYLES = {
                "asctime": {"bold": True, "color": "black"},
                "levelname": {"bold": True, "color": "red"},
            }
        elif self.log_level == "WARNING":
            coloredlogs.DEFAULT_FIELD_STYLES = {
                "asctime": {"bold": True, "color": "black"},
                "levelname": {"bold": True, "color": "yellow"},
            }
        elif self.log_level == "DEBUG":
            coloredlogs.DEFAULT_FIELD_STYLES = {
                "asctime": {"bold": True, "color": "black"},
                "levelname": {"bold": True, "color": "blue"},
            }
        else:
            coloredlogs.DEFAULT_FIELD_STYLES = {
                "asctime": {"bold": True, "color": "black"},
                "levelname": {"bold": True, "color": "blue"},
            }
        coloredlogs.DEFAULT_LOG_FORMAT = "%(levelname)s: %(asctime)s | %(message)s"

        coloredlogs.install(level=self.log_level, logger=logger)
        logger.propagate = self.propogate
        return logger

    def get_message(self, message, details: Optional[Union[list, dict]] = None):
        try:
            if isinstance(message, (list, dict)):
                if self.local:
                    message = json.dumps(message, indent=4, cls=JsonHelper)
                else:
                    message = json.dumps(message, cls=JsonHelper)
            if details:
                if message[-1] != ":":
                    message = f"{message}:"
                if isinstance(details, (list, dict)):
                    if self.local:
                        details = json.dumps(details, indent=4, cls=JsonHelper)
                    else:
                        details = json.dumps(details, cls=JsonHelper)
                message = f"{message}\n{details}"
            return message
        except Exception:
            return message

    def info(self, message, details: Optional[Union[list, dict]] = None):
        message = self.get_message(message, details)
        self.log().info("%s", message)

    def debug(self, message, details: Optional[Union[list, dict]] = None):
        message = self.get_message(message, details)
        self.log().debug("%s", message)

    def warning(self, message, details: Optional[Union[list, dict]] = None):
        message = self.get_message(message, details)
        self.log().warning("%s", message)

    def error(self, message, details: Optional[Union[list, dict]] = None):
        message = self.get_message(message, details)
        self.log().error("%s", message)

    def output(self, values: dict):
        wrkdir = os.getcwd()
        file_path = "output_logs.json"
        with open(file_path, "w", encoding="utf-8") as out_file:
            out_file.write(json.dumps(values, indent=4, cls=JsonHelper))
        self.log().info("Logs output to: %s/%s", wrkdir, file_path)
