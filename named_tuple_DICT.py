from collections import namedtuple
def convert(dictionary):
    return namedtuple('GenericDict', dictionary.keys())(**dictionary)


print convert(dict(c=1,d=2))


def convert2(dictionary):
    NT = namedtuple('GenericDict', dictionary.keys())
    gen_dict = NT(**dictionary)
    return gen_dict


print convert2({'c':1, 'd':2})
print convert({'c':1, 'd':2})
