import datetime
from datetime import datetime, timedelta, date
import time
import json

import calendar

start = '1480446000000'  # START: 2016-11-29 19:00:00,
stop = '1480447500000'  # STOP: 2016-11-29 19:25:00
start_time = time.gmtime(float(start) / 1000.)
stop_time = time.gmtime(float(stop) / 1000.)

print "START: {0}, STOP: {1}".format(
    time.strftime('%Y-%m-%d %H:%M:%S', start_time),
    time.strftime('%Y-%m-%d %H:%M:%S', stop_time)
)


def get_timestamp(d):
    if isinstance(d, date) and not isinstance(d, datetime):
        d = datetime.combine(d, datetime.time(0, 0, 0, 0))

    msec = str(d.microsecond).rjust(6).replace(' ', '0')

    return float('%s.%s' % (calendar.timegm(d.utctimetuple()), msec))

five_min = timedelta(minutes=5)
stop_time2_dt = datetime.utcnow()
start_time2_dt = stop_time2_dt - five_min

print "START: {0}, STOP: {1}".format(
    start_time2_dt.strftime('%Y-%m-%d %H:%M:%S'),    #datetime.strftime('%Y-%m-%d %H:%M:%S', start_time2_dt),
    stop_time2_dt.strftime('%Y-%m-%d %H:%M:%S') #datetime.strftime('%Y-%m-%d %H:%M:%S', stop_time2_dt)
)

# stop_time2 = time.gmtime(float(get_timestamp(stop_time2_dt)))
# start_time2 = time.gmtime(float(get_timestamp(start_time2_dt)))

# timestamp
stop_time2 = int(get_timestamp(stop_time2_dt) * 1000)
start_time2 = int(get_timestamp(start_time2_dt) * 1000)

print 'stop_time2_dt', stop_time2_dt, 'start_time2_dt', start_time2_dt


import signalfx
flow = signalfx.SignalFx().signalflow('y0z1mWizm2m-ae4Erm15ag')

program = "failed_check_statuses = data('asg.healthy.infinite-loop.failed-check-status.TEST', extrapolation='zero')" \
                 ".not_between(200, 399, True, True)" \
                 ".publish(label='failed_check_statuses')"



c = flow.execute(program, start=start_time2, stop=stop_time2)

for msg in c.stream():
    if isinstance(msg, signalfx.signalflow.messages.DataMessage):
        data = msg.data
        print('@data {0}: {1}'.format(msg.logical_timestamp_ms, str(json.dumps(data))))

        print ' {0:<19} | {1:<12} | {2:<34} | {3:<17} | {4:<50} | {5:<16} | {6}'.format('timestamp', 'key',
                                                                                        'AWSUniqueId',
                                                                                        'service',
                                                                                        'host',
                                                                                        'host_ip',
                                                                                        'val')

        for datapoint_key, datapoint_val in msg.data.iteritems():
            if datapoint_val > 0:
                print (' {0:<19} | {1:<12} | {2:<34} | {3:<17} | {4:<50} | {5:<16} | {6}'.format(
                    time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(float(msg.logical_timestamp_ms) / 1000.)),
                    datapoint_key,
                    c.get_metadata(datapoint_key)['AWSUniqueId'],
                    c.get_metadata(datapoint_key)['app'],
                    c.get_metadata(datapoint_key)['host'],
                    c.get_metadata(datapoint_key)['host_ip'],
                    datapoint_val))

    elif isinstance(msg, signalfx.signalflow.messages.MetadataMessage):
        print('@metadata {0}: {1}'.format(str(msg.tsid), str(msg.properties)))

    elif isinstance(msg, signalfx.signalflow.messages.InfoMessage):
        print('@info {0}: {1}'.format(msg.logical_timestamp_ms, str(msg)))

    elif isinstance(msg, signalfx.signalflow.messages.EventMessage):
        print('@event {0}: {1}'.format(msg.timestamp_ms, msg.properties))

    else:
        print('not interested: {0}'.format(msg))

"""
print "---------"
# T - 5min$
five_min = timedelta(minutes=5)
start_time2_dt = datetime.utcnow()
stop_time2_dt = start_time2_dt - five_min
start_time2 = time.gmtime(time.mktime(start_time2_dt.timetuple()))
stop_time2 =  time.gmtime(time.mktime(stop_time2_dt.timetuple()))


print "START: {0}, STOP: {1}".format(
    time.strftime('%Y-%m-%d %H:%M:%S', start_time2),
    time.strftime('%Y-%m-%d %H:%M:%S', stop_time2)
)

print '------'
print time.gmtime(0)
print start_time2
print start_time2_dt
print calendar.timegm(start_time2 ) * 1000
print calendar.timegm(start_time2 )

"""
"""
1480446000000
1481079436000
"""
"""

print "-----"

start3 = '1481057894522'  # START: 2016-11-29 19:00:00,
stop3 = '1481079669000'  # STOP: 2016-11-29 19:25:00
start_time3 = time.gmtime(float(start3) / 1000.)
stop_time3 = time.gmtime(float(stop3) / 1000.)

print "START: {0}, STOP: {1}".format(
    time.strftime('%Y-%m-%d %H:%M:%S', start_time3),
    time.strftime('%Y-%m-%d %H:%M:%S', stop_time3)
)
"""