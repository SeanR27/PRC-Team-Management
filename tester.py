import pandas as pd

from . import columns as cols
from .actions import globalData as gd

from .actions import players
from .actions import teams
from .actions import weeksTable
from .actions import weeklyGames
from .actions import weeklyStats


df = pd.DataFrame(columns = ["Number", "Name"])
df.loc[len(df)] = [0, "Sean"]
df.loc[len(df)] = [1, "Rodriguez"]
df.loc[len(df)] = [2, "Karly"]
df.loc[len(df)] = [3, "Gillian"]
df.loc[len(df)] = [4, "Isabelle"]
df.loc[len(df)] = [5, "Luis"]
df.loc[len(df)] = [6, "Coquito"]

gd.loadSequence()
weeksTable.addWeek("ORC", 0, 20261024)
weeksTable.addWeek("Milton", 1, 20261031)
weeksTable.addWeek("Cedar", 0, 20261107)
weeksTable.addWeek("ORC", 1, 20261114)
weeksTable.addWeek("TS", 0, 20261121)
weeksTable.addWeek("TS", 0, 20261121)