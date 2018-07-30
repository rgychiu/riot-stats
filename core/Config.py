import json


class Config:

    CREDENTIALS_PATH = "credentials.json"
    CONFIG_PATH = "config.json"
    DEFAULTS_KEY = "defaults"

    def __init__(self):
        # Get credentials
        with open(self.CREDENTIALS_PATH, 'rU') as cred_file:
            self.credentials = json.load(cred_file)

        # Load defaults json
        with open(self.CONFIG_PATH, 'rU') as config_file:
            self.config = json.load(config_file)

    def get_defaults(self):
        return self.config[self.DEFAULTS_KEY]
