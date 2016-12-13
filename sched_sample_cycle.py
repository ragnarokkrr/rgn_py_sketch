import schedule
import time_serializable


def print_omg():
    print "OMG"

schedule.every(2).seconds.do(print_omg)


while(True):
    schedule.run_pending()
    time_serializable.sleep(1)




