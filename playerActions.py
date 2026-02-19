import pandas as pd
import os

os.chdir("C:/Users/seanr/Documents/5 - PRC Software")

def main():
    playerCSV_path = "players.csv"
    playerPKL_path = "players.pkl"

    df = getDF(playerPKL_path)
    df = clearTable(df)
    df = addPlayer(df, "Agota", "Roth")
    print(df)
    #export(df, "players.csv", "players.pkl")


# Ipmort & Export Functions
def getDF(path): return pd.read_pickle(path)
def getDF_csv(path): return pd.read_csv(path)
def export(df, csv_exp_path, pkl_exp_path): df.to_csv(csv_exp_path, index = False); df.to_pickle(pkl_exp_path)

def getColumnDict():
    # KeyName : [index, columnLabel]
    return {"playerID": [0, "PLAYER_ID"],
            "firstName": [1, "FIRST"],
            "lastName": [2, "LAST"],
            "totalGames": [3, "TOT_GAMES"],
            "positionGames": [4, "POS_GAMES"],
            "wins": [5, "WIN"],
            "losses": [6, "LOSS"],
            "ties": [7, "TIE"],
            "performance": [8, "PERF"],
            "weightedScore": [9, "WS"]
            }

def clearTable(df): return df.drop(df.index, inplace = False)

def addPlayer(df, first, last):

    first = first.capitalize()
    last = last.capitalize()

    colDict = getColumnDict()

    rows = len(df)

    maxID = -1
    if not df.empty:
        maxID = int(df[colDict["playerID"][1]].max()[1:])

    df.loc[rows, colDict["playerID"][1]] = "P" + str(maxID + 1).zfill(4)
    df.loc[rows, colDict["firstName"][1]] = first
    df.loc[rows, colDict["lastName"][1]] = last

    return df





main()