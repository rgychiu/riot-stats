import json


class Config:

    # Default file paths
    CREDENTIALS_PATH = "credentials.json"
    CONFIG_PATH = "config.json"

    # Defaults and credentials
    API_KEY = "api_key"
    DEFAULTS_KEY = "defaults"
    DEFAULT_QUEUE_ID = "queue_id"

    def __init__(self):
        # Get credentials
        with open(self.CREDENTIALS_PATH, 'rU') as cred_file:
            self.credentials = json.load(cred_file)

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
