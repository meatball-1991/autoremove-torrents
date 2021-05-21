from flexget import plugin
from flexget.entry import Entry
from flexget.event import event

from .autoremovetorrents.FlexgetExcute import Executor

import json


class autoremove:
    schema = {
        "type": "object",
        "properties": {
            "qbittorrent": {"type": "object", "properties": {},},
            "view": {"type": "boolean", "default": False},
            "debug": {"type": "boolean", "default": False},
            "delete_data": {"type": "boolean", "default": False},
            "strategies": {"type": "object", "properties": {}},
        },
        "additionalProperties": False,
    }

    def on_task_output(self, task, config):
        config["name"] = task.name
        config["client"] = "qbittorrent"
        config["username"] = config["qbittorrent"]["username"]
        config["password"] = config["qbittorrent"]["password"]
        if config["qbittorrent"]["use_ssl"]:
            config["host"] = (
                "https://"
                + config["qbittorrent"]["host"]
                + ":"
                + str(config["qbittorrent"]["port"])
            )
        else:
            config["host"] = (
                "http://"
                + config["qbittorrent"]["host"]
                + ":"
                + str(config["qbittorrent"]["port"])
            )
        # json_str = json.dumps(config)
        with open("./text.txt", "a") as f:
            # f.write(json_str)
            f.write(task.name)
        Executor.autoremove(config)


@event("plugin.register")
def register_plugin():
    plugin.register(autoremove, "autoremove", api_ver=2)
