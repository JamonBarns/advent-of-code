games = {}

max_cubes ={
    "red": 12,
    "green": 13,
    "blue": 14
}

with open("input", "r") as f:
    for game in f:
        game_id = game.split(":")[0].split(" ")[1]
        rounds = game.split(":")[1].split(";")
        games[game_id] = []
        for i in range(0,len(rounds)):
            round_result = rounds[i].strip().split(", ")
            new_round = {}
            for index in range(0,len(round_result)):
                new_round[round_result[index].split(" ")[1]] = int(round_result[index].split(" ")[0])

            games[game_id].append(new_round)


#print(games)
possible_games = []

for game in games:
    game_impossible = False
    print(games[game])
    for round in games[game]:
        for cube_result in round:
            if round[cube_result] > max_cubes[cube_result]:
                game_impossible = True

    if not game_impossible: possible_games.append(int(game))


print(games)
        
print(sum(possible_games))