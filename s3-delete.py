import boto3
import datetime
import calendar
import operator
import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--bucket", help = "Name of bucket")
parser.add_argument("--x", help = "Last number of deployments")

args = parser.parse_args()

_PREFIX = '/'

s3 = boto3.resource('s3')

bucket = s3.Bucket(args.bucket)
x_keep = int(args.x)

result = bucket.meta.client.list_objects(Bucket=bucket.name, Delimiter='/')


# Dictionary of deployments
deployments = {}

# Populate deployments into dictionary with timestamp by index.html
for o in result.get('CommonPrefixes'):
   deploy_id = o.get('Prefix')
   print (deploy_id)
   index = s3.Object(bucket.name, "{}index.html".format(deploy_id))
   deployments[deploy_id] = (calendar.timegm(index.last_modified.timetuple()))


sorted_deployments = sorted( deployments.items(), key=operator.itemgetter(1), reverse=True)


# delete last X

deleted_deployments = sorted_deployments[x_keep:]
print ("Deployments to delete")
print (deleted_deployments)

for deployment in deleted_deployments:
   bucket.objects.filter(Prefix=deployment[0]).delete()
