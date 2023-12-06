class CardScatcher:
    def __init__(self, line: str) -> None:
        self.line = line
        self.card_id = -1
        self.winning_numbers = set()
        self.card_numbers = []
        self._parse_input()

    def _parse_input(self) -> None:
        card_data = self.line.split(":")
        assert len(card_data) == 2

        temp = card_data[0].split(" ")
        card_id = ""
        for value in temp:
            value = value.strip()
            if value.isdigit():
                card_id = value
                break
            

        try:
            self.card_id = int(card_id)
        except Exception as e:
            print(f"error: {card_id}")
            print(f"card_data: {card_data[0]}")
            raise e

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
    
    def count_winning_numbers(self) -> int:
        wins = 0
        
        for n in self.card_numbers:
            if n in self.winning_numbers:
                wins += 1

        return wins


def num_cards() -> int:
    total_cards = 0
    
    card_map = {}
    card_list = []
    card_queue = []
    with open("day04b/data/input") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            card = CardScatcher(line=line)
            card_map[card.card_id] = card
            card_list.append(card)
            card_queue.append(card)
            
    card_count = [1] * len(card_list)
    
    for card in card_list:
        assert isinstance(card, CardScatcher)
        wins = card.count_winning_numbers()
        
        for i in range(wins):
            card_count[card.card_id + i] += card_count[card.card_id-1] 
        

    return sum(card_count)



print(num_cards())
