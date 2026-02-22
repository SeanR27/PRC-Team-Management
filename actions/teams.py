import pandas as pd
import os

from .. import fileManagement as fm
from .. import columns as cols

def main():
    None

def createTable():
    colDict = cols.teams()
    df = pd.DataFrame(columns = [colDict["teamID"][1],
                                    colDict["teamName"][1]
                                    ])

def clearTable(df): return df.drop(df.index, inplace = False)

main()