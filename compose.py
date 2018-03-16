class compose:
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
            return self
        else:
            return self.func(other)


def _compose_helper(f, g):
    return lambda *args, **kwargs: f(g(*args, **kwargs))

