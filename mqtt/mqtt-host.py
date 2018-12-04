
# coding: utf-8

# In[ ]:


import paho.mqtt.publish as publish
import time
import numpy as np

HOST = "192.168.1.192"
PORT = 1883

epoch = 0
squence_num = 0
while(epoch<5):
    for i in np.arange(5):
        print("RPI %i speaks..." % i)
        print("MSG %i" % squence_num)
        publish.single("UWB", "%i%i"% (i, squence_num), hostname=HOST)
        squence_num += 1
        time.sleep(2)
    epoch +=1

