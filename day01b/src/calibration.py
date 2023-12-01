
digit_str_digit_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def get_first_digit(line: str) -> str:   
    line_length = len(line) 
    for i,s in enumerate(line):
        # Check if value is a simple digit character
        if s.isdigit():
            return s
        
        # Read the next values in the string and see if it matches the digit map
        current_value = ""
        # Read next 3 letters and check map
        if i + 3 < line_length:
            current_value = f"{line[i]}{line[i+1]}{line[i+2]}"
            if current_value in digit_str_digit_map:
                return digit_str_digit_map[current_value]
        # Append the 4th letter and check map
        if i + 4 < line_length:
            current_value = f"{current_value}{line[i+3]}"
            if current_value in digit_str_digit_map:
                return digit_str_digit_map[current_value]
        # Append the 5th letter and check map
        if i + 5 < line_length:
            current_value = f"{current_value}{line[i+4]}"
            if current_value in digit_str_digit_map:
                return digit_str_digit_map[current_value]
            
    return "0"

def get_last_digit(line: str) -> str:
    line_length = len(line) - 1
    for i,s in enumerate(reversed(line)):
        if s.isdigit():
            return s

        # Reads the characters in reverse order and checks map
        # For example three will be read as the following
        # ree
        # hree
        # and finally three
        # This is super ugly and i dont like it but i cant think of a nicer way right now
        current_value = ""
        if line_length - i - 3 >= 0:
            current_value = f"{line[line_length - i - 2]}{line[line_length - i - 1]}{line[line_length - i]}"
            if current_value in digit_str_digit_map:
                return digit_str_digit_map[current_value]
        if line_length - i - 4 >= 0:
            current_value = f"{line[line_length - i - 3]}{current_value}"
            if current_value in digit_str_digit_map:
                return digit_str_digit_map[current_value]
        if line_length - i - 5 >= 0:
            current_value = f"{line[line_length - i - 4]}{current_value}"
            if current_value in digit_str_digit_map:
                return digit_str_digit_map[current_value]
        
    
    return "0"
    

def read_calibration() -> int:
    calibration = 0
    
    with open('day01b/data/input') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            # Find first digit in line
            first_digit = get_first_digit(line=line)
            # Find last digit in line
            last_digit = get_last_digit(line=line)
            # Combine into int
            num = int(f"{first_digit}{last_digit}")
            calibration += num
        
    
    return calibration

print(read_calibration())