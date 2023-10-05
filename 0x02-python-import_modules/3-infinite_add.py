#!/usr/bin/python3
if __name__ == "__main__":
    import sys, math
    total = 0
    for i in sys.argv[1:]:
        total += int(i)
        print("{}".format(total))
