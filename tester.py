import pandas as pd

df = pd.DataFrame(columns = ["Number", "Name"])
df.loc[len(df)] = [0, "Sean"]
df.loc[len(df)] = [1, "Rodriguez"]
df.loc[len(df)] = [2, "Karly"]
df.loc[len(df)] = [3, "Gillian"]
df.loc[len(df)] = [4, "Isabelle"]
df.loc[len(df)] = [5, "Luis"]
df.loc[len(df)] = [6, "Coquito"]

print(df["Number"].values.__class__)