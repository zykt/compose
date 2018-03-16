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


def test_complex_composition():
    from functools import partial

    @compose
    def first(l): return l[0]

    @compose
    def second(l): return l[1]

    @compose
    def is_title(s): return s.istitle()

    @compose
    def id(x): return x

    filter_by_first_sort_by_second = id >> partial(filter, first >> is_title) >> partial(sorted, key=second >> abs)

    assert filter_by_first_sort_by_second([('Hello', 10), ('NOCAPS', -8), ('Welcome', 9), ('speaklouder', 80)]) == \
        [('Welcome', 9), ('Hello', 10)]
