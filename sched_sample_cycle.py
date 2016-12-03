import schedule
import time


def print_omg():
    print "OMG"

schedule.every(2).seconds.do(print_omg)


while(True):
    schedule.run_pending()
    time.sleep(1)




