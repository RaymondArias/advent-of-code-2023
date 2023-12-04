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

    def can_play_game(self, red_cubes=12, green_cubes=13, blue_cubes=14) -> bool:
        # checks whether this game is possible

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

                # if any of the counts is greater than the initial cube count this game is not possible
                if (
                    red_count > red_cubes
                    or green_count > green_cubes
                    or blue_count > blue_cubes
                ):
                    return False

        return True


def count_cubes() -> int:
    id_count = 0
    with open("day02a/data/input") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()

            # Read each line into a Game instance
            game = Game(game_line=line)

            # see if game is possible
            if game.can_play_game():
                # If possible add this game_id to id_count
                id_count += game.game_id

    return id_count


print(count_cubes())
