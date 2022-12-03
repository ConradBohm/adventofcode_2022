game = open("input.txt", "r")
game_rounds = game.read().split("\n")
game.close()

# A&X == Rock, B&Y == Paper, C&Z == Scissors

score = 0
mapping = {"A X": 3, "A Y": 6, "A Z": 0,
           "B X": 0, "B Y": 3, "B Z": 6,
           "C X": 6, "C Y": 0, "C Z": 3}

for round in game_rounds:
    round = list(round)
    if round[2] == "X":
        score += 1
    elif round[2] == "Y":
        score += 2
    elif round[2] == "Z":
        score += 3

score += sum([mapping[i] for i in game_rounds])
print(score) # part 1
