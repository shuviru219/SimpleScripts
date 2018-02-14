import boto3
#import datetime
from datetime import *
import requests

client = boto3.client('cloudtrail')
def lambda_handler(event, context):
    # TODO implement
    print "invoked  cloudwatch "
    #print str(event)
    now = datetime.now()
    tyear= now.year
    tmonth= now.month
    tday= now.day
    thour= now.hour
    thourold=thour-1
    tmin= now.minute
    tsec= now.second
    response = client.lookup_events(
    LookupAttributes=[
        {
            'AttributeKey': 'EventName',
            'AttributeValue': 'UpdateFunctionCode20150331v2'
        },
    ],
    StartTime=datetime(tyear,tmonth, tday, thourold, 0, 0),
    EndTime=datetime(tyear,tmonth, tday,thour, 0, 0),
    MaxResults=123,
    #NextToken='string '
    )
    
    
    #print datetime(2018,2, 12, 7, 6, 9)
    lens=len(response['Events'])
    print lens
    #print   response['Events'][0]['EventTime']
    for j in range(lens):
        #for i in range(lens):
        #print response['Events'][0]
        eventtime= response['Events'][j]['EventTime']
        eventname=response['Events'][j]['EventName']
        
        uname= response['Events'][j]['Username']
        rsrc= response['Events'][j]['Resources'][0]['ResourceName']
        #print rsrc
        msgstr="User "+str(uname) + " Updated Lambda "+ str(rsrc) +" on " + str(eventtime)
        WEBHOOK_URL="https://hooks.slack.com/services/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"
        payload = {
            'text': msgstr,
            'channel': "general",
            'username': "shuvam",
            }
        
        r = requests.post(WEBHOOK_URL, json=payload)
        #print r.status_code
        #return 'Hello from Lambda  '
        
