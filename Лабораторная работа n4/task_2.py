import csv
import json


input_filename = "input.csv"
output_filename = "output.json"


def task(input_filename, output_filename) -> None:
    json_array = []
    with open(input_filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            json_array.append(row)

    with open(output_filename, "w") as json_file:
        json_str = json.dumps(json_array, indent=4)
        json_file.write(json_str)


if __name__ == '__main__':
    task(input_filename, output_filename)

    with open(output_filename) as output_f:
        for line in output_f:
            print(line, end="")

