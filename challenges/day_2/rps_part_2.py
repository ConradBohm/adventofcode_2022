game = open("input.txt", "r")
game_rounds = game.read().split("\n")
game.close()

score = 0
shape_score_mapping = {
    "A":{
        "X": 3,
        "Y": 1,
        "Z": 2
    },
    "B":{
        "X": 1,
        "Y": 2,
        "Z": 3
    },
    "C":{
        "X": 2,
        "Y": 3,
        "Z": 1
    }
}

for round in game_rounds:
    round = list(round)
    score += shape_score_mapping[round[0]][round[2]]

    if round[2] == "X":
        score += 0
    elif round[2] == "Y":
        score += 3
    elif round[2] == "Z":
        score += 6

print(score)