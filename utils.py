import platform
import json


class PingLibrary:

    def __init__(self):
        self.__current_platform = platform.system()

    def get_ping_command(self) -> str:
        with open("platform-system.json", "r") as file:
            json_config = json.load(file)
        try:
            return json_config[self.__current_platform]
        except KeyError:
            return ""
