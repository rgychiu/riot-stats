# TODO: Create endpoints for web app to be able to query analyzed data
from analysis.ChampionAnalyzer import ChampionAnalyzer
from analysis.MatchAnalyzer import MatchAnalyzer
from flask import Flask, request
from api.utils import *

# Instantiate necessary classes
app = Flask(__name__)
champ_analyzer = ChampionAnalyzer()
match_analyzer = MatchAnalyzer()

# URL ENDPOINTS, CONSTANTS
_MAX_LEN_RETURN = 10
_GET_CHAMPION_WINRATE = '/winrate/<champion_name>'
_GET_MATCHUP_WINRATE = '/winrate/matchup'

# TODO: Catch errors
@app.route(_GET_CHAMPION_WINRATE)
def get_champion_winrate(champion_name):
    return create_response(data=champ_analyzer.champion_winrate(champion_name), status=200)

@app.route(_GET_MATCHUP_WINRATE)
def get_matchup_winrate():
    first_champ = request.args.get('champion_one')
    second_champ = request.args.get('champion_two')
    return create_response(data=match_analyzer.matchup_winrate(first_champ,second_champ), status=200)
