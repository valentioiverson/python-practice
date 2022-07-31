def print_formatted(number):
    # your code goes here
    w = len("{0:b}".format(number))
    for i in range(1, number+1):
        print("{i:{w}d} {i:{w}o} {i:{w}X} {i:{w}b}".format(i=i, w=w))

