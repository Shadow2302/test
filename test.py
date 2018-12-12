def print_error():
    print("ti tupoi?")


try:
    a = int(input("Enter your age: "))
    if a >= 0 and a <= 115:
    print("Your year of birth is {}".format(2018 - a))
    else:
        print_error()
except Exception:
    print_error()
