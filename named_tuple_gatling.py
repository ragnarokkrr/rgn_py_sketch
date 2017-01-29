from collections import namedtuple

GlobalInfoMetric = namedtuple('GlobalInfoMetric', [
            'request_count',
            'min_response_time',
            'max_response_time',
            'mean_response_time',
            'std_deviation',
            'response_time_50th_percentile',
            'response_time_75th_percentile',
            'mean_requests_sec'])

ResponseTimeDistribution = namedtuple('ResponseTimeDistribution', [
            'time_lt_800',
            'time_bt_800_1200',
            'time_gt_1200',
            'failed'])

GlobalInfoMetricDescription = GlobalInfoMetric (request_count= 'request count',
    min_response_time = 'min response time',
    max_response_time = 'max response time',
    mean_response_time = 'mean response time',
    std_deviation = 'std deviation',
    response_time_50th_percentile = 'response time 50th percentile',
    response_time_75th_percentile = 'response time 75th percentile',
    mean_requests_sec = 'mean requests/sec'
)


ResponseTimeDistributionDescription = ResponseTimeDistribution(
    time_lt_800 = 't < 800 ms',
    time_bt_800_1200 = '800 ms < t < 1200 ms',
    time_gt_1200 = 't > 1200 ms',
    failed = 'failed'
)

print set(GlobalInfoMetricDescription.__dict__.itervalues())

print set(ResponseTimeDistributionDescription.__dict__.itervalues())

print ResponseTimeDistributionDescription
