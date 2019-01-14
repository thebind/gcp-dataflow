#Import pubsub libraries
from google.cloud import pubsub
import time

#setup publisher client
publisher=pubsub.PublisherClient()

#setup topic to publish to.
topic='projects/universal-code-210021/topics/test-topic'

#Publish to topic 10 times with a sleep in between for 2 seconds.
for n in range(1,10):
    data =  time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
	
    #actual publishing step
    publisher.publish(topic,data)
    print('Published data : ',data)
    time.sleep(2)
	
