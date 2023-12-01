import re

# numeric_dict = {'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r', 'five': 'f5e', 'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'}
numeric_dict = {
    "twone": 21,
    "sevenine": 79,
    "eightwo": 82,
    "eighthree": 83,
    "oneight": 18,
    "threeight": 38,
    "fiveight": 58,
    "nineight": 98,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    
}

def replace_numbers_in_string(input_string, numeric_dict):
    for key, value in numeric_dict.items():
        input_string = input_string.replace(key, str(value))
    return input_string

# Define the file's name.
filename = "day1input.txt"

numbers = []
totalSum = 0

# Open the file and read its content.
with open(filename) as f:
    content = f.read().splitlines()

# Display the content.
for line in content:
    resultString = replace_numbers_in_string(line, numeric_dict)
    numInLine = re.findall(r'\d', resultString)
    num = int(numInLine[0] + numInLine[-1])
    totalSum += num

print(totalSum)