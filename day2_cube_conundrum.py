class Game:

    def __init__(self, input):
        input = input.replace("Game ", "")
        first_split = input.split(":")
        self.id = int(first_split[0])

        mini_games = first_split[1].split(";")
        self.red = int(0)
        self.green = int(0)
        self.blue = int(0)
        for mini_game in mini_games:
            # mini_game =" 3 blue, 4 red"
            pulls = mini_game.split(",")
            for pull in pulls:
                pull = pull.strip()
                dice = pull.split(" ")
                if dice[1] == "red":
                    self.red = self._max(self.red, int(dice[0]))
                if dice[1] == "green":
                    self.green = self._max(self.green, int(dice[0]))
                if dice[1] == "blue":
                    self.blue = self._max(self.blue, int(dice[0]))
    
    def is_possible(self, constraint):
        if constraint["red"] >= self.red and constraint["green"] >= self.green and constraint["blue"] >= self.blue:
            return True
        return False

    def _max(self, num1, num2):
        if num1 > num2:
            return num1
        return num2

def puzzle1():
    f = open("input2.txt", "r")
    items = f.read()

    sum_ids = 0
    for item in items.split("\n"):    
        constraint = { "red": 12, "green": 13, "blue": 14 }
        print(item)
        game = Game(item)
        if game.is_possible(constraint):
            sum_ids += game.id
    return sum_ids

def puzzle2():
    f = open("input2.txt", "r")
    items = f.read()
    power_sum = 0
    for item in items.split("\n"):
        game = Game(item)
        power_sum += game.red * game.green * game.blue
    return power_sum
print(puzzle2())