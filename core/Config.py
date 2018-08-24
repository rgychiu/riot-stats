import json
from core.Singleton import Singleton


class Config(Singleton):

    # Default file paths
    DEFAULT_CREDENTIALS_PATH = "credentials_path"
    LOG_PATH_KEY = "log_path"
    CONFIG_PATH = "config.json"

    # Defaults and credentials
    API_KEY = "api_key"
    DEFAULTS_KEY = "defaults"
    DEFAULT_QUEUE = "queue"
    DEFAULT_QUEUE_ID = "queue_id"

    def __init__(self, cred_path=None):
        super().__init__()

        # Load defaults json
        with open(self.CONFIG_PATH, 'rU') as config_file:
            self.config = json.load(config_file)

        # Get credentials
        self.credentials_file = cred_path or self.get_default_credentials_path()
        with open(self.credentials_file, 'rU') as file:
            self.credentials = json.load(file)

    def get_default_credentials_path(self):
        return self.config[self.DEFAULT_CREDENTIALS_PATH]

    def get_default_log_path(self):
        return self.config[self.LOG_PATH_KEY]

    def get_defaults(self):
        return self.config[self.DEFAULTS_KEY]

    def get_api_key(self):
        return self.credentials[self.API_KEY]

    def get_defaults_queue(self):
        return self.get_defaults()[self.DEFAULT_QUEUE]

    def get_defaults_queue_id(self):
        return self.get_defaults()[self.DEFAULT_QUEUE_ID]
