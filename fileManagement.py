import pandas as pd
import os

def getDF_pkl(path): return pd.read_pickle(path)
def getDF_csv(path): return pd.read_csv(path)
def export(df, csv_path, pkl_path): df.to_csv(csv_path, index = False); df.to_pickle(pkl_path)
def make_pkl(csv_path, pkl_path): df = getDF_csv(csv_path); df.to_pickle(pkl_path)
