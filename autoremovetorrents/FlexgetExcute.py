#!/usr/bin/python3
# -*- coding:utf-8 -*-
import sys
import getopt
import traceback
import yaml

from . import logger
from .task import Task
from .version import __version__


class Executor:
    @staticmethod
    def autoremove(config):
        # Set default logging path to current working directory
        log_path = "./"

        # Decide whether to output debug log
        debug_mode = config["debug"]

        # Init logger
        logger.Logger.init(
            log_path, file_debug_log=debug_mode, output_debug_log=debug_mode
        )
        lg = logger.Logger.register(__name__)

        # Run autoremove
        try:
            # Show version
            lg.debug("Auto Remove Torrents %s" % __version__)

            # Run task
            try:
                Task(config["name"], config, not config["view"]).execute()
            except Exception:
                lg.error(traceback.format_exc().splitlines()[-1])
                lg.error("Task %s fails. " % config["name"])
                lg.debug("Exception Logged", exc_info=True)
        except Exception:
            lg.error(traceback.format_exc().splitlines()[-1])
            lg.debug("Exception Logged", exc_info=True)
            lg.critical(
                "An error occured. If you think this is a bug or need help, you can submit an issue."
            )

