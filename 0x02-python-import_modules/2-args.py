#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num_args = len(sys.argv) - 1

    if num_args > 1:
        print("{} arguments:".format(num_args))
        count = 1
        for arg in sys.argv[1:]:
            print("{}: {}".format(count, arg))
            count += 1
    elif num_args == 1:
        print("{} argument:".format(num_args))
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments.".format(num_args))
