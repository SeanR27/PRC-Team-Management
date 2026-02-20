import os

rootPath = os.path.dirname(__file__).replace('\\', '/') + "/"

def mainPath(): return rootPath
def dataPath(): return rootPath + "data/"
def playerPath(): return dataPath() + "players/"
def weeksPath(): return dataPath() + "weeks/"
def teamsPath(): return dataPath() + "teams/"
def weekGamesPath(): return dataPath() + "week_games/"
def weekStatsPath(): return dataPath() + "week_player_stats/"