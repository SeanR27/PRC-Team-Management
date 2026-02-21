# KeyName : [index, columnLabel]

def players():
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

def weeks():
    """
    The Column Lable-Index dictionary for the weeks.csv table.
    This table holds each week ID.
    """
    return {"weekID": [0, "WEEK_ID"],
            "OppID": [1, "OPP_TEAM_ID"],
            "homeAway": [2, "H_A"],
            "date": [3, "DATE"]
            }

def teams():
    return {"teamID": [0, "TEAM_ID"],
            "teamName": [1, "TEAM_NAME"]
            }

def weeklyGames():
    """
    The Label-Index dictionary for a week's game table columns.
    These tables hold games information for some week.
    """
    return {"courtNum": [0, "COURT"],
            "player1": [1, "P1"],
            "player2": [2, "P2"],
            "pairStrength": [3, "PAIR_STRNGTH"],
            "result": [4, "RESULT"]
            }

def weeklyStats():
    """
    The Label-Index dictionary for a weekly stats table columns.
    These tables hold player information for some week.
    """
    return {"playerID": [0, "PLAYER_ID"],
            "court_ass": [1, "COURT_ASSIGNED"],
            "court_played": [2, "COURT_PLAYED"],
            "result": [3, "RESULT"],
            "ws_before": [4, "WS_BEFORE"],
            "ws_after": [5, "WS_AFTER"],
            "weekAvab": [6, "AVAB"]
            }

def initialData():
    """
    The Column Label-Index dictionary for the initial data table columns.
    """
    return {"firstName": [0, "FIRST"],
            "lastName": [1, "LAST"],
            "court": [2, "COURT_ASS"]
            }