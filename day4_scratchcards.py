class Lottery:
    def __init__(self, input):
        split_card = input.split(":")
        self.id = int(split_card[0])
        split_numbers = split_card[1].strip().split("|")        
        self.left_numbers = self._get_left_numbers(split_numbers[0].strip())
        self.winning_numbers = self._get_winning_numbers(split_numbers[1].strip())

    def _get_left_numbers(self, numbers_input):
        return [int(x) for x in numbers_input.split(" ") if x.isdigit()]
    
    def _get_winning_numbers(self, numbers_input):
        return [(int(x)) for x in numbers_input.split(" ") if x.isdigit() and int(x) in self.left_numbers]

def puzzle1():
    f = open("input4.txt", "r")
    items = f.read()

    sum = 0
    for item in items.split("\n"):
        lottery = Lottery(item.replace("Card ", ""))
        if len(lottery.winning_numbers) > 0:
            sum += 2**(len(lottery.winning_numbers) - 1)
    return sum

def puzzle2():
    f = open("input4.txt", "r")
    items = f.read()
    items_split = items.split("\n")
    sum = [1] * len(items_split)
    total_sum = 0
    for item in items_split:
        lottery = Lottery(item.replace("Card ", ""))
        
        for i in range(len(lottery.winning_numbers)):
            if lottery.id + i < len(items_split):
                sum[lottery.id + i] += sum[lottery.id - 1]
        total_sum += sum[lottery.id - 1]
    return total_sum

print(puzzle1())
print(puzzle2())