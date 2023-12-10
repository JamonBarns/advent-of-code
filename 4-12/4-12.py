import os

FILE_NAME = os.environ.get("FILE")

def file_to_list():
    list = []
    with open(FILE_NAME, "r") as file:
        for line in file: list.append(line.strip('\n'))
        return list
    
card_list = file_to_list()

for card in card_list:
    wn = []
    for i in card.split(": ")[1].split(" | ")[0].split(" "):
        if i != "": wn.append(int(i))
    pn = []
    for i in card.split(": ")[1].split(" | ")[1].split(" "):
        if i != "": pn.append(int(i))
    new_card = {
        "game": card.split(": ")[0],
        "winning_numbers": wn,
        "picked_numbers": pn
    }
    card_list[card_list.index(card)] = new_card

for card in card_list:
    points = 0
    for picked_number in card["picked_numbers"]:
        if picked_number in card["winning_numbers"]:
            if points == 0: points += 1
            else: points *= 2
    card_list[card_list.index(card)]["points"] = points

total_points = 0

for card in card_list: total_points += card["points"]

print(total_points)

# Part 2
for card in card_list:
    points = 0
    for picked_number in card["picked_numbers"]:
        if picked_number in card["winning_numbers"]:
            points += 1
    card["additional_cards"] = []
    for point in range(0,points):
        card["additional_cards"].append(card_list[card_list.index(card) + (point + 1)])
    card_list[card_list.index(card)] = card
    for additional_card in card["additional_cards"]:
        card_list[card_list.index(card)] = card

def count_cards(card_list, card_count = 0):
    for card in card_list:
        card_count += len(card["additional_cards"])
        card_count = count_cards(card["additional_cards"], card_count)
    return card_count

print(count_cards(card_list) + len(card_list))
