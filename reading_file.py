stats = {}

errors = 0


def print_error():
    print("ti tupoi?")


def smart_int(string):
    new_string = ""
    for symbol in string:
        if symbol >= '0' and symbol <= '9':
            new_string += symbol
        else:
            pass
    return int(new_string)


def smart_int_display(num):
    string = str(num)
    new_string = ""
    i = 1
    for sym in string[::-1]:
        if i == 3:
            new_string += sym + " "
            i = 1
        else:
            new_string += sym
            i += 1
    return new_string[::-1]


with open("text.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        name, points = line.split(":")
        stats.setdefault(name, 0)
        try:
            stats[name] += smart_int(points)
        except ValueError:
            print_error()
            errors += 1

winner = ""
total = 0
for name, points in stats.items():
    if points > total:
        total = points
        winner = name

print("The winner is {} with {} points.\n{} errors occured.".format(
    winner, smart_int_display(total), errors))
