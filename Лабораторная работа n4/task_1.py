# TODO решите задачу
import json
with open("input.json") as file:
    file_input = json.load(file)


def task() -> float:
    sum_of_elements = 0
    for value in file_input:
        sum_of_elements += value['score'] * value['weight']

    return round(sum_of_elements,3)


print(task())
