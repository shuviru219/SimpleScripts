#! /usr/bin/python
#
import sys
import os
import time
import boto.ec2.connection

# args are instance id, device,
# mount-host tag value, and mount-name tag value
#
if (5 != len(sys.argv)):
    print 'Missing or extra argument!'
    exit(1)
iid = sys.argv[1]
dvc = sys.argv[2]
mhost = sys.argv[3]
mname = sys.argv[4]

# Get the access key, and secret key
#
f = open('/secrets/setup/ak', 'r')
ak = f.readline()
f.close()
f = open('/secrets/setup/sk', 'r')
sk = f.readline()
f.close()

# Connect to EC2
#
c = boto.ec2.connection.EC2Connection(
  aws_access_key_id=ak,
  aws_secret_access_key=sk)

# Find the volume to mount
#
mvol = None
filter = { 'tag:mount-host' : mhost }
vols = c.get_all_volumes(filters = filter)
for vol in vols:
    vid = vol.id
    tfilter = { 'resource-id' : vid, 'key' : 'mount-name' }
    tags = c.get_all_tags(tfilter)
    if (0 == len(tags)):
        continue
    if (tags[0].value != mname):
        continue
    mvol = vol
    break

if (mvol == None):
    print "No volume found with matching tags"
    exit(1)

# Attach the volume
#
status = c.attach_volume(mvol.id, iid, dvc)
if ('attaching' != status):
    print "attach_volume returned '{0}'".format(status)
    print "Could not attach volume"
    exit(2)
dev_suffix = dvc[6:]
device = "/dev/xv" + dev_suffix
for x in range(1,10):
    ok = False
    try:
        s = os.stat(device)
        ok = True
    except:
        print "device {0} does not yet exist".format(device)
        pass
    if True == ok:
        print "attached."
        exit(0)
    time.sleep(2)
print "Timed out trying to attach the volume"
exit(3)