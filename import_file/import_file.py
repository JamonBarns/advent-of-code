import os

FILE_NAME = os.environ.get("FILE")

def file_to_list():
    list = []
    with open(FILE_NAME, "r") as file:
        for line in file: list.append(line)
        return list