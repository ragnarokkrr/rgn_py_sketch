from bidict import bidict
from collections import namedtuple


element_by_symbol = bidict(H='hydrogen')

print element_by_symbol

print element_by_symbol['H']

print element_by_symbol.inv['hydrogen']

print element_by_symbol.inv.inv is element_by_symbol


print '=' * 50



GlobalInfoMetric = namedtuple('GlobalInfoMetric', [
            'request_count',
            'min_response_time',
            'max_response_time',
            'mean_response_time',
            'std_deviation',
            'response_time_50th_percentile',
            'response_time_75th_percentile',
            'mean_requests_sec'])

GlobalInfoMetricDescription = GlobalInfoMetric (request_count= 'request count',
    min_response_time = 'min response time',
    max_response_time = 'max response time',
    mean_response_time = 'mean response time',
    std_deviation = 'std deviation',
    response_time_50th_percentile = 'response time 50th percentile',
    response_time_75th_percentile = 'response time 75th percentile',
    mean_requests_sec = 'mean requests/sec'
)



infoMetrics = bidict()

for k,v in GlobalInfoMetricDescription.__dict__.iteritems():
    print k, v
    infoMetrics.put(k, v)


print infoMetrics

print infoMetrics['response_time_75th_percentile']

print infoMetrics.inv['response time 75th percentile']


print infoMetrics.keys()
print infoMetrics.values()
print (isinstance([] ,list))
print (isinstance(GlobalInfoMetricDescription, GlobalInfoMetric))
print {k: v for (k,v) in GlobalInfoMetricDescription._asdict().iteritems()}
