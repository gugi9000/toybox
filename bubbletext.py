
def myfunc(string):
    beta = ''
    for x, y in enumerate(string):
        if x % 2 == 0:
            beta = beta + y.upper()
        else:
            beta = beta + y.lower()
    return beta

print(myfunc('abcdefghijklmnopqrstuvwxyz'))
print(myfunc('FOO BAR BAZ drOOl DRool woot woOt wOOt'))

