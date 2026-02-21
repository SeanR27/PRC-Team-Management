import pandas as pd
import os

from .. import fileManagement as fm
from .. import columns as cols

def main():
    df = fm.getDF_pkl(fm.mainDataPath(2, 2))
    print(df)
    #fm.export(df, config.mainDataPath(1, 2), config.mainDataPath(2, 2))

def clearTable(df): return df.drop(df.index, inplace = False)

main()