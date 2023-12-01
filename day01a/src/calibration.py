def get_first_digit(line: str) -> str:
    for s in line:
        if s.isdigit():
            return s
    return "0"


def get_last_digit(line: str) -> str:

    for s in reversed(line):
        if s.isdigit():
            return s

    return "0"


def read_calibration() -> int:
    calibration = 0

    with open("day01a/data/input") as f:
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
