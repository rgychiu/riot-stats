import json


class Config:

    CREDENTIALS_PATH = "credentials.json"
    CONFIG_PATH = "config.json"
    API_KEY = "api_key"
    DEFAULTS_KEY = "defaults"
    LEAGUE_KEY = "league_id"
    START_SUMM_KEY = "summoner_name"

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
