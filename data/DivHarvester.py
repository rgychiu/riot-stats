from data.Harvester import Harvester


class DivHarvester(Harvester):

    def __init__(self):
        super().__init__()

    def get_sr_challenger_league(self):
        """
        Get list of all challenger tier players.
        :return: API JSON response for challenger players
        """
        return self.make_request(self.get_challenger_path() + self.config_manager.get_defaults_queue_id())


