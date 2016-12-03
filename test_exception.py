import logging
import sys


def test_handling():
    print "test_handling()"
    raise RuntimeError("My Erro ")


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

    try:
        test_handling()
    except:
        e = sys.exc_info()[0]
        logging.error("error: " + str(e))


