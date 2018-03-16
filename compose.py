class Compose:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __rshift__(self, other):
        self.func = _compose_helper(other, self.func)
        return self

    def __rrshift__(self, other):
        if callable(other):
            self.func = _compose_helper(self.func, other)
        else:
            self.func = self.func(other)
        return self

compose = Compose


def _compose_helper(f, g):
    return lambda *args, **kwargs: f(g(*args, **kwargs))


@compose
def add1(x): return x + 1
@compose
def mul10(x): return x * 10

add1mul10 = add1 >> mul10


print(add1mul10(1))

print(((lambda x: x / 2) >> add1)(10))

