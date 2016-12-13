import sched
import time_serializable


scheduler = sched.scheduler(time_serializable.time_serializable, time_serializable.sleep)


def print_event(name):
    print "EVENT:", time_serializable.time_serializable(), name


print 'START', time_serializable.time_serializable()

scheduler.enter(2, 1, print_event, ('first',))
scheduler.enter(3, 1, print_event, ('second',))

scheduler.run()
