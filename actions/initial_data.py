import pandas as pd
import os

from .. import fileManagement as fm
from .. import columns as cols

def main():
    df = createTable()
    fm.export(df, fm.mainDataPath(1,3), fm.mainDataPath(2,3))

def createTable():
    colDict = cols.initialData()
    df = pd.DataFrame(columns = [   colDict["firstName"][1],
                                    colDict["lastName"][1],
                                    colDict["court"][1]])
    return df

def clearTable(df): return df.drop(df.index, inplace = False)

main()