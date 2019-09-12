#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    if argc == 1:
        """ zero arguments """
        print("{} arguments.".format(len(sys.argv) - 1))
    elif argc == 2:
        print("{} argument:".format(argc - 1))
        print("{}: {}".format(argc - 1, sys.argv[1]))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))

        for index, data in enumerate(sys.argv, start=1):
            print("{}: {}".format(index, data))
