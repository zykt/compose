from compose import compose


@compose
def add1(x):
    return x + 1


@compose
def mul2(x):
    return x * 2


# equivalent to mul2(add1(1))
assert 1 >> add1 >> mul2 == 4


@compose
def real(c):
    return c.real()


@compose
def negative(x):
    return x <= 0


# find all complex numbers with their real parts < 0
assert list(filter(real >> negative, [1+2j, 3, -1-1j, 4j])) == [-1-1j, 4j]
