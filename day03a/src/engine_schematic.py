from typing import List


class EngineSchematic:
    def __init__(self) -> None:
        # 2d array that holds schematic input
        self.schematic = []
        self.schematic_num = {}

    def read_line(self, line: str) -> None:
        line_list = []

        for value in line:
            line_list.append(value)

        self.schematic.append(line_list)

    def get_schematic_number(self) -> int:
        schematic_number = 0

        for i, line in enumerate(self.schematic):
            for j, value in enumerate(line):
                value = str(value)
                # Check if value is a symbol
                if not value.isdigit() and value != ".":
                    # Get all adjacent numbers and add to sum
                    adjacent_nums = self._find_adjacent_nums(i, j)
                    for n in adjacent_nums:
                        schematic_number += n

        return schematic_number

    def _find_adjacent_nums(self, i: int, j: int) -> List:
        adjacent_nums = []

        # Check row above
        if i - 1 >= 0 and self.schematic[i - 1][j] != ".":
            adjacent_nums.append(self._read_num(i=i - 1, j=j))
        # Check row below
        if i + 1 <= len(self.schematic) - 1 and self.schematic[i + 1][j] != ".":
            adjacent_nums.append(self._read_num(i=i + 1, j=j))
        # Check column to left
        if j - 1 >= 0 and self.schematic[i][j - 1] != ".":
            adjacent_nums.append(self._read_num(i=i, j=j - 1))
        # Check column to right
        if j + 1 <= len(self.schematic[0]) - 1 and self.schematic[i][j + 1] != ".":
            adjacent_nums.append(self._read_num(i=i, j=j + 1))
        # Check diagonal, row above and column to left
        if i - 1 >= 0 and j - 1 >= 0 and self.schematic[i - 1][j - 1] != ".":
            adjacent_nums.append(self._read_num(i=i - 1, j=j - 1))
        # Check diagonal, row above and column to right
        if (
            i - 1 >= 0
            and j + 1 <= len(self.schematic[i]) - 1
            and self.schematic[i - 1][j + 1] != "."
        ):
            adjacent_nums.append(self._read_num(i=i - 1, j=j + 1))
        # Check diagonal, row below and column to left
        if (
            i + 1 <= len(self.schematic) - 1
            and j - 1 >= 0
            and self.schematic[i + 1][j - 1] != "."
        ):
            adjacent_nums.append(self._read_num(i=i + 1, j=j - 1))
        # Check diagonal, row below and column to right
        if (
            i + 1 <= len(self.schematic) - 1
            and j + 1 <= len(self.schematic[i]) + 1
            and self.schematic[i + 1][j + 1] != "."
        ):
            adjacent_nums.append(self._read_num(i=i + 1, j=j + 1))

        return adjacent_nums

    def _read_num(self, i: int, j: int) -> int:
        # Find the start and ending index
        start_index = j
        end_index = j

        while start_index >= 0 and self.schematic[i][start_index].isdigit():
            if start_index - 1 < 0 or not self.schematic[i][start_index - 1].isdigit():
                break
            start_index += -1
        while (
            end_index < len(self.schematic[i]) - 1
            and self.schematic[i][end_index].isdigit()
        ):
            if (
                end_index + 1 > len(self.schematic[i]) - 1
                or not self.schematic[i][end_index + 1].isdigit()
            ):
                break
            end_index += 1

        value = ""
        if start_index < 0:
            start_index = 0
        if end_index >= len(self.schematic[i]):
            end_index = len(self.schematic[i]) - 1

        for x in range(start_index, end_index + 1):
            value = f"{value}{self.schematic[i][x]}"
            # Mark the value as visited
            self.schematic[i][x] = "."

        return int(value)


def schematic_number() -> int:
    schematic = EngineSchematic()
    with open("day03a/data/input") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            schematic.read_line(line)

    return schematic.get_schematic_number()


print(schematic_number())
