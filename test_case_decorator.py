import unittest



def data_provider(data):

    if callable(data):
        data = data()

    if not all(isinstance(i, tuple) for i in data):
        raise Exception("Need a sequence of tuples as data...")

    def test_decorator(fn):
        def test_decorated(self, *args):
            for i in data:
                try:
                    fn(self, *(i + args))
                except AssertionError as e:
                    raise AssertionError (e.message + " data set used: %s " % repr(i))
        return test_decorated
    return test_decorator


def expect_exception(exception):
    def test_decorator(fn):
        def test_decorated(self, *args, **kwargs):
            self.assertRaisees(exception, fn, self, *args, **kwargs)
        return test_decorated
    return test_decorator


class MyTestcase(unittest.TestCase):

    @data_provider((("A",), ("0",),))
    def test_value_error(self, value):
        int(value)


if __name__ == '__main__':
    unittest.main()