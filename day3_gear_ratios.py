# Set SPECIAL_CHARS for puzzle1
# Set SPECIAL_CHARS_2 for puzzle2

SPECIAL_CHARS = "-@#$%&*=+/"
SPECIAL_CHARS_2 = "*"

class Input:
    def __init__(self, number, start_location, end_location):
        self.number = number
        self.is_part_number = False
        self.start_location = start_location
        self.end_location = end_location
    
    def set_is_part_number(self):
        self.is_part_number = True

class InputSpecial:
    def __init__(self, special_char, location):
        self.special_char = special_char
        self.location = location
        self.numbers = []
        self.has_gear = False
        self.numbers_multiplied = 0
    
    def add_number(self, number):
        self.numbers.append(number)
        if len(self.numbers) == 2:
            self.has_gear = True
            self.numbers_multiplied = self.numbers[0] * self.numbers[1]

class InputLine:    
    def __init__(self, input, previous_line):
        self.previous_line = previous_line
        (self.inputs, self.specials) = self._calculate_inputs(input)        
        self.inputs = self._calculate_part_numbers(self.inputs, self.specials, self.previous_line)
        if self.previous_line:
            self.previous_line.inputs = self._calculate_previous_part_numbers(self.previous_line.inputs, self.specials)

    def _calculate_previous_part_numbers(self, previous_inputs, specials):
        for input in previous_inputs:
            for special in specials:
                if (input.start_location - 1) <= special.location and (input.end_location + 1) >= special.location:
                        input.set_is_part_number()
                        special.add_number(input.number)
        return previous_inputs

    def _calculate_part_numbers(self, inputs, specials, previous_line):
        for input in inputs:
            for special in specials:
                if input.start_location - 1 == special.location or input.end_location + 1 == special.location:
                    input.set_is_part_number()
                    special.add_number(input.number)
            
            if previous_line:
                for special in previous_line.specials:
                    if (input.start_location - 1) <= special.location and (input.end_location + 1) >= special.location:
                        input.set_is_part_number()
                        special.add_number(input.number)

        return inputs
    
    def _calculate_inputs(self, input):
        new_inputs = []
        specials = []
        i = 0        
        while i < len(input):
            number = 0
            start_location = 0
            end_location = 0
            digit_counter = 0

            while i < len(input) and input[i].isdigit():
                if digit_counter == 0:
                    start_location = i
                end_location = i
                number = int(input[i]) + (number * 10)
                digit_counter += 1
                i += 1
                if i == len(input) or not input[i].isdigit():
                    new_inputs.append(Input(number, start_location, end_location))

            if i < len(input) and input[i] in SPECIAL_CHARS_2:
                specials.append(InputSpecial(input[i], i))
            
            i += 1

        return new_inputs, specials

def puzzle1():
    f = open("input3.txt", "r")
    items = f.read()

    prev = None
    sum = 0
    for item in items.split("\n"):
        new_input = InputLine(item, prev)
        if prev:
            for input in prev.inputs:
                if input.is_part_number:
                    sum += input.number
        prev = new_input
    
    for input in prev.inputs:
        if input.is_part_number:
            sum += input.number
    return sum

def puzzle2():    
    f = open("input3.txt", "r")
    items = f.read()

    prev = None
    sum = 0
    for item in items.split("\n"):
        new_input = InputLine(item, prev)
        if prev:
            for special in prev.specials:
                if special.has_gear:
                    sum += special.numbers_multiplied
        prev = new_input
    
    for special in prev.specials:
        if special.has_gear:
            sum += special.numbers_multiplied
    return sum

print(puzzle2())