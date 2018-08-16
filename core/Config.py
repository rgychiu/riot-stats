import json


class Config:

    # Default file paths
    DEFAULT_CREDENTIALS_PATH = "credentials_path"
    CONFIG_PATH = "config.json"

    # Defaults and credentials
    API_KEY = "api_key"
    DEFAULTS_KEY = "defaults"
    DEFAULT_QUEUE_ID = "queue_id"

    def __init__(self, cred_path=None):
        # Get credentials
        self.credentials_file = cred_path or self.DEFAULT_CREDENTIALS_PATH
        with open(self.credentials_file, 'rU') as file:
            self.credentials = json.load(file)

        # Load defaults json
        with open(self.CONFIG_PATH, 'rU') as config_file:
            self.config = json.load(config_file)

    def get_defaults(self):
        return self.config[self.DEFAULTS_KEY]

    def get_api_key(self):
        return self.credentials[self.API_KEY]

    def get_defaults_queue_id(self):
        return self.get_defaults()[self.DEFAULT_QUEUE_ID]

    def get_defaults_summoner(self):
        return self.get_defaults()[self.START_SUMM_KEY]
