def simple_generator():
    yield 1
    yield 2
    yield 3


def test_simple_generator():
    generator = simple_generator()

    print next(generator)
    print next(generator)
    print next(generator)


def my_gen(n):
    yield n
    yield n + 1


def test_my_gen():
    g = my_gen(6)

    print next(g)
    print next(g)
    print next(g)


def zero_one_generator():
    i = 0
    while True:
        yield i
        i = (i + 1) % 2


def test_one_zero():
    zero_one = zero_one_generator()
    print next(zero_one)
    print next(zero_one)
    print next(zero_one)
    print next(zero_one)
    print next(zero_one)


def slice_generator():
    i = 0
    while True:
        yield 0 if (i <= 3) else 1
        i = i + 1 if (i <= 3) else i


def test_slice_zero():
    slice_item = slice_generator()
    print next(slice_item)
    print next(slice_item)
    print next(slice_item)
    print next(slice_item)
    print next(slice_item)


if __name__ == '__main__':
    #  test_simple_generator()
    # test_my_gen()

    test_slice_zero()

    #  slice = slice_generator()
    import itertools
    print list(itertools.islice(slice_generator(), 19))





"""
def zero_one_generator():
    i = 0
    while True:
        yield i
        i = (i + 1) % 2


zero_one_gen = zero_one_generator()

check_health_results = [default_check_health(),
                        timed_out_check_health()]
"""