from google.cloud import pubsub
import time
import random

#setup publisher client
publisher=pubsub.PublisherClient()
#setup topic to publish to.
topic='projects/universal-code-210021/topics/test-topic'
productsList = ['Macbook','WindowsPC','LinuxPC']
while True:
     product = productsList[random.randint(0,2)]
     price = random.randint(1000,2000)
     currTS = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
     print('Publishing Data %s %i %s' % (product,price,currTS))
     data = '%s,%i' % (product,price)
     publisher.publish(topic,data)
     time.sleep( random.randint(1,3))
