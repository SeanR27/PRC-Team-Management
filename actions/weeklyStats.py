import pandas as pd
import os

from .. import config
from .. import fileManagement as fm

rootPath = config.mainPath()
dataPath = config.dataPath()
weeks_dataPath = config.weeksPath()
weeksGames_dataPath = config.weekGamesPath()
weekStats_dataPath = config.weekStatsPath()
thisPath = os.path.dirname(__file__)

def main():
    None

def getColumnDict():
    """
    The Column Lable-Index dictionary for a week table.
    These tables hold information about each game for some week.
    """
    return {"playerID": [0, "PLAYER_ID"],
            "court_ass": [1, "COURT_ASSIGNED"],
            "court_played": [2, "COURT_PLAYED"],
            "result": [3, "RESULT"],
            "ws_before": [4, "WS_BEFORE"],
            "ws_after": [4, "WS_AFTER"],
            "weekAvab": [4, "AVAB"]
            }

def createWeek(weekID):
    colDict = getColumnDict()
    newDF = pd.DataFrame(columns = [colDict["playerID"][1],
                                    colDict["court_ass"][1],
                                    colDict["court_played"][1],
                                    colDict["result"][1],
                                    colDict["ws_before"][1],
                                    colDict["ws_after"][1],
                                    colDict["weekAvab"][1]])
    
    weekStatsID = "WPS_" + weekID
    pathBase = weekStats_dataPath + weekStatsID + "/"
    
    os.makedirs(pathBase, exist_ok = True)
    fm.export(newDF, pathBase + weekStatsID + ".csv", pathBase + weekStatsID + ".pkl")

main()