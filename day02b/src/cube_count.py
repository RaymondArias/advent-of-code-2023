class Game:
    def __init__(self, game_line: str) -> None:
        self.game_line = game_line
        self.game_id = -1
        self.game_sets = []
        self._parse_game_line()

    def _parse_game_line(self) -> None:
        # Split input by : to get game_id and game_result
        game_data = self.game_line.split(sep=":")

        assert len(game_data) == 2
        # Get game_id
        self.game_id = int(game_data[0].split(" ")[1])

        # Get sets in the games
        self.game_sets = game_data[1].split(";")

    def cube_power(self) -> int:
        min_red = 0
        min_green = 0
        min_blue = 0

        # Iterate through all sets of this game
        for set in self.game_sets:
            set = set.strip()
            cubes = set.split(",")

            # Count the number of occurences for each cube
            red_count = 0
            green_count = 0
            blue_count = 0
            for cube in cubes:
                cube = cube.strip()
                cube_data = cube.split(" ")

                cube_count = int(cube_data[0])
                cube_color = cube_data[1]

                if cube_color == "blue":
                    blue_count += cube_count
                if cube_color == "red":
                    red_count += cube_count
                if cube_color == "green":
                    green_count += cube_count

            min_red = max(min_red, red_count)
            min_blue = max(min_blue, blue_count)
            min_green = max(min_green, green_count)
        return min_red * min_blue * min_green


def count_cubes() -> int:
    sum_of_power = 0
    with open("day02b/data/input") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()

            # Read each line into a Game instance
            game = Game(game_line=line)
            sum_of_power += game.cube_power()

    return sum_of_power


print(count_cubes())
