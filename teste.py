def pqp():
    return "a"


AAAA = pqp()


def aaa():
    def b():
        return 'aaa b'


a = {}

if __name__ == '__main__':
    a['a'] = 2222

    print a
    print AAAA