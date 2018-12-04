
# coding: utf-8

# In[ ]:


import paho.mqtt.publish as publish
import time
import numpy as np

HOST = "192.168.1.187"
PORT = 1883

epoch = 0
while(epoch<5):
    for i in np.arange(5):
        print("RPI %i speaks..." % i)
        publish.single("UWB", "%i"% i, hostname=HOST)
        time.sleep(2)
    epoch +=1

