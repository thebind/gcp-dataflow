#Import pubsub libraries
from google.cloud import pubsub
import time

#setup the subscriber
subscriber = pubsub.SubscriberClient()

#setup callback function to receive and process message
def callback(message):
    print('Received message: {}'.format(message))
	#acknowledge the message. The same client will not get the message again.
    message.ack()

#subscription to subscribe to
subscription='projects/universal-code-210021/subscriptions/test-subscription'

#subscribe and hookup with callback function. Will be called everytime a 
#new message comes in
future = subscriber.subscribe(subscription,callback)

print('Starting to Listen {}'.format(subscription))

#Sleep to keep the program alive.
while True:
    time.sleep(50)

	
	

