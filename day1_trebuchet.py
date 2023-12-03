f = open("input.txt", "r")
items = f.read()

def part1(items):
    sum = 0
    for item in items.split("\n"):
        has_first = False
        first = 0
        last = 0
        for letter in item:
            if letter.isdigit():
                if not has_first:
                    first = int(letter)
                    has_first = True
                last = int(letter)
        sum += (first*10 + last)        
    
    return sum

def part2(items):    
    sum = 0
    for item in items.split("\n"):
        has_first = False
        first = 0
        last = 0
        print(item)
        item = replace_all_string_numbers(item)
        print(item)
        for letter in item:
            if letter.isdigit():
                if not has_first:
                    first = int(letter)
                    has_first = True
                last = int(letter)
        sum += (first*10 + last)        
    
    return sum

def replace_all_string_numbers(item):
    if "zero" in item:
        item = replace_string_with_number(item, "zero", "0ero")
    if "one" or "on8" in item:
        item = replace_string_with_number(item, "one", "1ne")
        item = replace_string_with_number(item, "on8", "1n8")
    if "two" or "tw1" in item:
        item = replace_string_with_number(item, "two", "2wo")
        item = replace_string_with_number(item, "tw1", "2w1")
    if "three" or "thre8" in item:
       item = replace_string_with_number(item, "three", "3hree")
       item = replace_string_with_number(item, "thre8", "3hre8")
    if "four" in item:
        item = replace_string_with_number(item, "four", "4our")
    if "five" or "fiv8" in item:
        item = replace_string_with_number(item, "five", "5ive")
        item = replace_string_with_number(item, "fiv8", "5iv8")
    if "six" in item:
        item = replace_string_with_number(item, "six", "6ix")
    if "seven" or "seve9" in item:
        item = replace_string_with_number(item, "seven", "7even")
        item = replace_string_with_number(item, "seve9", "7eve9")
    if "eight" or "eigh2" or "eigh3" in item:
        item = replace_string_with_number(item, "eight", "8ight")
        item = replace_string_with_number(item, "eigh2", "8igh2")
        item = replace_string_with_number(item, "eigh3", "8igh3")
    if "nine" or "nin8" in item:
        item = replace_string_with_number(item, "nine", "9ine")
        item = replace_string_with_number(item, "nin8", "9in8")
    return item

def replace_string_with_number(item, string_number, number):    
    item = item.replace(string_number, number)
    return item

print(part2(items))