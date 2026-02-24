import pandas as pd
import os

from .actions import globalData as gd

# Import & Export Tools
def getDF_pkl(path): return pd.read_pickle(path)
def getDF_csv(path): return pd.read_csv(path)
def export(df, csv_path, pkl_path): df.to_csv(csv_path, index = False); df.to_pickle(pkl_path)
def make_pkl(csv_path, pkl_path): df = getDF_csv(csv_path); df.to_pickle(pkl_path)

# File Path Tools
rootPath = os.path.dirname(__file__).replace('\\', '/') + "/"

def mainPath(): return rootPath
def dataPath(): return rootPath + "data/"

def mainDataPath(mode, dataName):
    """
    Returns the path for accessing principal data files.

    Mode:
        0 : path to directory
        1 : path to CSV file
        2 : path to PKL file
    """
    dataName_str = str(dataName)
    if dataName_str not in gd.mainDataNames:
        raise Exception("There is no main data file that should have root filename: " + dataName_str)
        
    if mode == 0: return dataPath() + dataName_str + "/"
    elif mode == 1: return mainDataPath(0, dataName_str) + dataName_str + ".csv"
    elif mode == 2: return mainDataPath(0, dataName_str) + dataName_str + ".pkl"
    return None

def weekGamesPath(mode, weekID):
    """
    Returns the path to a week of games table.

    mode:
        0 : general directory for all week of games
        1 : direcotry for specific week of games
        2 : CSV file path for specific week of games table
        3 : PKL file path for specific week of games table

    weekID:
        The week ID for the path.
        If None, mode is automatically set to 0.
    """
    dirName = "week_games/"

    if (weekID == None) or (mode == 0): return dataPath() + dirName
    
    if mode == 1: return weekGamesPath(0, None) + weekID + "/"
    if mode == 2: return weekGamesPath(0, None) + weekID + "/" + weekID + ".csv"
    if mode == 3: return weekGamesPath(0, None) + weekID + "/" + weekID + ".pkl"
    else:
        print("Failed to get week of games path." + "\nWeek ID: " + weekID + "\nMode: " + str(mode))

def weekStatsPath(mode, weekID):
    """
    Returns the path to the player stats for a given week.

    mode:
        0 : general directory for all weekly stats
        1 : direcotry for stats of specific week
        2 : CSV file path for stats of specific week
        3 : PKL file path for stats of specific week

    weekID:
        The week ID for the path.
        If None, mode is automatically set to 0.
    """
    dirName = "week_player_stats/"

    if (weekID == None) or (mode == 0): return dataPath() + dirName
    else: weekStatsID = "WPS_" + weekID
    
    if mode == 1: return weekStatsPath(0, None) + weekStatsID + "/"
    if mode == 2: return weekStatsPath(0, None) + weekStatsID + "/" + weekStatsID + ".csv"
    if mode == 3: return weekStatsPath(0, None) + weekStatsID + "/" + weekStatsID + ".pkl"
    else:
        print("Failed to get weekly stats path." + "\nWeek ID: " + weekID + "\nMode: " + str(mode))
