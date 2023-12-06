class CardScatcher:
    def __init__(self, line: str) -> None:
        self.line = line
        self.card_id = ""
        self.winning_numbers = set()
        self.card_numbers = []
        self._parse_input()

    def _parse_input(self) -> None:
        card_data = self.line.split(":")
        assert len(card_data) == 2

        self.card_id = card_data[0].split(" ")[1]

        card_value = card_data[1].strip()

        num_data = card_value.split("|")
        winning_nums = num_data[0].strip()
        winning_nums = winning_nums.split(" ")
        for n in winning_nums:
            n = n.strip()
            self.winning_numbers.add(n)

        card_nums = num_data[1].strip()
        card_nums = card_nums.split(" ")

        for num in card_nums:
            num = num.strip()
            if num.isdigit():
                self.card_numbers.append(num)

    def total_points(self) -> int:
        points = 0
        found_first = False

        for n in self.card_numbers:
            if n in self.winning_numbers:
                if not found_first:
                    points = 1
                    found_first = True
                else:
                    points = 2 * points

        return points


def card_winning() -> int:
    total_points = 0
    with open("day04a/data/input") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            card = CardScatcher(line=line)
            total_points += card.total_points()
    return total_points


print(card_winning())
