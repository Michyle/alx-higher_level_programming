#!/usr/bin/python3

if__name__ == "__main__":
    import sys

    count = lens(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for 1 in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1}))
