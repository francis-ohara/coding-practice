# https://www.algoexpert.io/questions/tournament-winner

def tournamentWinner(competitions, results):
    scoreboard = {}

    for i in range(len(competitions)):
        if results[i]:
            scoreboard[competitions[i][0]] = scoreboard.get(competitions[i][0], 0) + 1
        else:
            scoreboard[competitions[i][1]] = scoreboard.get(competitions[i][1], 0) + 1

    winner = None

    for player in scoreboard:
        if winner == None:
            winner = player
        else:
            if scoreboard[player] > scoreboard[winner]:
                winner = player

    return winner
