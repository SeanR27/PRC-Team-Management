# KeyName : [index, columnLabel]

def players():
    return {"playerID": [0, "PLAYER_ID"],
            "firstName": [1, "FIRST"],
            "lastName": [2, "LAST"],
            "court_ass": [3, "COURT"],
            "totalGames": [4, "TOT_GAMES"],
            "positionGames": [5, "POS_GAMES"],
            "wins": [6, "WIN"],
            "losses": [7, "LOSS"],
            "ties": [8, "TIE"],
            "performance": [9, "PERF"],
            "weightedScore": [10, "WS"]
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
    return {"weekID": [0, "WEEK_ID"],
            "courtNum": [1, "COURT"],
            "player1": [2, "P1"],
            "player2": [3, "P2"],
            "pairStrength": [4, "PAIR_STRNGTH"],
            "result": [5, "RESULT"]
            }

def weeklyStats():
    """
    The Label-Index dictionary for a weekly stats table columns.
    These tables hold player information for some week.
    """
    return {"weekID": [0, "WEEK_ID"],
            "playerID": [1, "PLAYER_ID"],
            "court_ass": [2, "COURT_ASSIGNED"],
            "court_played": [3, "COURT_PLAYED"],
            "result": [4, "RESULT"],
            "ws_before": [5, "WS_BEFORE"],
            "ws_after": [6, "WS_AFTER"],
            "weekAvab": [7, "AVAB"]
            }

def initialData():
    """
    The Column Label-Index dictionary for the initial data table columns.
    """
    return {"firstName": [0, "FIRST"],
            "lastName": [1, "LAST"],
            "court_ass": [2, "COURT_ASS"]
            }