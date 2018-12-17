stats = {
    "Alex": 0,
    "Bob": 0,
    "Brex": 0
}

errors = 0


def print_error():
    print("ti tupoi?")


with open("text.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        name, points = line.split(":")
        try:
            stats[name] += int(points)
        except ValueError:
            print_error()
            errors += 1

winner = max(stats)

print("The winner is {} with {} points.\n{} errors occured.".format(
    winner, stats[winner], errors))
