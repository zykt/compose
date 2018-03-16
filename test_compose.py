from compose import compose



def test_compose_two_composable():
    @compose
    def add1(x): return x + 1

    @compose
    def mul10(x): return x * 10

    a1m10 = add1 >> mul10

    assert a1m10(1) == 20


def test_compose_function_and_composable():
    def add1(x): return x + 1

    @compose
    def mul10(x): return x * 10

    a1m10 = add1 >> mul10

    assert a1m10(1) == 20


def test_compose_composable_and_function():
    @compose
    def add1(x): return x + 1

    def mul10(x): return x * 10

    a1m10 = add1 >> mul10

    assert a1m10(1) == 20


def test_multiple_composables():
    @compose
    def lower(s: str):
        return s.lower()

    @compose
    def replace(s):
        return s.replace('l', 'Y')

    @compose
    def swap_case(s):
        return s.swapcase()

    composition = lower >> replace >> swap_case

    assert composition('hELlo') == "HEyyO"

