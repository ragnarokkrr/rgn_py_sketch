def aws_format_local_hostname(local_ip, region):
    local_ip_fmt = local_ip.replace('.', '-')
    local_dns = "ip-{0}.{1}.compute.internal".format(local_ip_fmt, region)
    return local_dns

local_ip = '172.28.129.15'
region = 'us-west-2'

print aws_format_local_hostname(local_ip, region)



get_ec2_id()




