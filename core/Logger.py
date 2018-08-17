import logging
from core.Config import Config


class Logger:

    def __init__(self):
        self.config = Config.get_instance()
        logging.basicConfig(filename=self.config.get_default_log_path(), level=logging.INFO,
                            format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    def debug(self, message):
        logging.debug(message)

    def info(self, message):
        logging.info(message)

    def warning(self, message):
        logging.warning(message)

    def error(self, message):
        logging.error(message)
