integers = range(0,10)

def loop_it(integers):

    even = []
    for i in intergers:
        if i % 2 == 0:
            even.append(i)
    return even

def filter_it(intergers):
    return filter(lambda x: x % 2 == 0, integers)


def is_even(x):
    return x % 2 == 0


def filter_it(integers):
    return filter(is_even, integers)

# wow!

even = [x for x in integers if x % 2 == 0]

squared = list(map(lambda x: x * x, integers))

# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squared2 = [x * x for x in integers]







