import os

FILE_NAME = os.environ.get("FILE")

def file_to_list():
    list = []
    with open(FILE_NAME, "r") as file:
        for line in file: list.append(line.strip('\n'))
        return list
    
engine_schematics = file_to_list()

part_number_list = []
part_number_coordinates_list = []
star_list = []

for schematic_line_index in range(0,len(engine_schematics)):
    checked_indexes = []
    for schematic_column_index in range(0,len(engine_schematics[schematic_line_index])):
        if engine_schematics[schematic_line_index][schematic_column_index].isdigit() and schematic_column_index not in checked_indexes:
            digit_list = ""
            start_index = (schematic_line_index, schematic_column_index)
            while engine_schematics[schematic_line_index][schematic_column_index].isdigit():
                digit_list += engine_schematics[schematic_line_index][schematic_column_index]
                checked_indexes.append(schematic_column_index)
                schematic_column_index += 1
            part_number_coordinates_list.append({"stared": False, "coordinates": (start_index, (schematic_line_index, schematic_column_index -1))})
            part_number_list.append(int(digit_list))
        elif engine_schematics[schematic_line_index][schematic_column_index] == "*":
            star_list.append((schematic_line_index,schematic_column_index))

for part_number_coordinates in part_number_coordinates_list:
    if part_number_coordinates["coordinates"][0][1] - 1 >= 0 and engine_schematics[part_number_coordinates["coordinates"][0][0]][part_number_coordinates["coordinates"][0][1] - 1] == "*":
        part_number_coordinates["stared"] = True
    
    if (part_number_coordinates["coordinates"][1][1] + 1 < len(engine_schematics[part_number_coordinates["coordinates"][0][0]]) and 
        engine_schematics[part_number_coordinates["coordinates"][0][0]][part_number_coordinates["coordinates"][1][1] + 1] == "*"):
            part_number_coordinates["stared"] = True

    

print(part_number_coordinates_list)
        




