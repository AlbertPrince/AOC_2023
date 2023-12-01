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
    keys = sorted(numeric_dict.keys(), key=len, reverse=True)

    for i in range(len(input_string)):
        for key in keys:
            if input_string.startswith(key, i):
                input_string = input_string[:i] + str(numeric_dict[key]) + input_string[i + len(key):]
                break  # Move to the next position in the outer loop

    return input_string

# Example usage
input_str = "4nine1bpdhrp86sfppzgbmtwonepbz"

result_str = replace_numbers_in_string(input_str, numeric_dict)
print(result_str)





