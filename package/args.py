import argparse
import requests

import os
import json

def my_metadata_user_data():
    user_data = {}

    def metadata_resolve_sources():
        parser = argparse.ArgumentParser()
        parser.add_argument('--debug-local-metadata', action='store_true')
        args = parser.parse_args()

        host = 'http://127.0.0.1:3000' if args.debug_local_metadata else 'http://169.254.169.254'
        user_file = os.path.join('c:\\', 'etc', 'reuters', 'user_data') if args.debug_local_metadata else '/etc/reuters/user_data'
        return host, user_file

    metadata_host, userdata_file_name = metadata_resolve_sources();

    def fetch_url(url):
        response = requests.get(url, timeout=10)
        return str(response.text)

    def instance_identity():
        url = metadata_host + '/latest/dynamic/instance-identity/document'
        response = requests.get(url, timeout=10)
        return response.json()

    def get_hostname():
        return fetch_url(metadata_host + '/latest/meta-data/hostname')

    def get_ip():
        return fetch_url(metadata_host + '/latest/meta-data/local-ipv4')

    def get_ec2_id():
        return fetch_url(metadata_host + '/latest/meta-data/instance-id')

    def local_user_data():
        try:
            with open(userdata_file_name) as f:
                user_data_file = f.read().splitlines()

            for line in user_data_file:
                if 'export' in line.strip():
                    key_value = line.replace('export', '').strip().split('=')
                    user_data[key_value[0]] = key_value[1]
        except Exception as e:
            raise Exception("Cannot load '%s'. Cause: %s" % (userdata_file_name, str(e)))

    def instance_metadata():
        user_data['EC2_HOSTNAME'] = get_hostname()
        user_data['EC2_ID'] = get_ec2_id()
        user_data['EC2_IPADDR'] = get_ip()
        user_data['EC2_INSTANCE'] = instance_identity()

    local_user_data()
    instance_metadata()

    return user_data


if __name__ == '__main__':
    user_data = my_metadata_user_data()
    print json.dumps(user_data, indent=4, sort_keys=True)


    print 'http://eureka.%s.%s.oneplatform.build:8080/v2/apps/' % (user_data['EC2_REGION'],
                                                                   user_data['CLOUD_ENVIRONMENT'])



