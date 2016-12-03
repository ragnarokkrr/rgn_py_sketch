import argparse
import requests




from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "ec2 moco!"

@app.route("/latest/meta-data/hostname")
def hostname():
    return "ip-172-28-198-122.us-west-2.compute.internal"

@app.route("/latest/meta-data/local-ipv4")
def ip():
    return "172.28.198.122"


@app.route("/latest/meta-data/instance-id")
def instanceid():
    return "i-aa53be6d"

@app.route("/latest/dynamic/instance-identity/document")
def insance_identity():
    return """{
          "devpayProductCodes" : null,
          "availabilityZone" : "us-west-2a",
          "privateIp" : "172.28.198.122",
          "version" : "2010-08-31",
          "instanceId" : "i-aa53be6d",
          "billingProducts" : null,
          "instanceType" : "t2.small",
          "accountId" : "246604972757",
          "pendingTime" : "2016-01-06T21:52:48Z",
          "imageId" : "ami-075b4066",
          "architecture" : "x86_64",
          "kernelId" : null,
          "ramdiskId" : null,
          "region" : "us-west-2"
        }
    """
if __name__ == '__main__':
    app.run(port=3000)
