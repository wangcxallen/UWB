
# coding: utf-8

# In[ ]:


import paho.mqtt.publish as publish
import time
import numpy as np

HOST = "192.168.1.235" #235 in arena/199 in home
PORT = 1884 #1884 in arena/1883 in home

epoch = 0
squence_num = 0
while(epoch<1000):
    for i in np.arange(4):
        print("RPI %i speaks..." % i)
        print("MSG %i" % squence_num)
        print("-"*30)
        publish.single("UWB", "%i%i"% (i, squence_num), hostname=HOST, port=PORT)
        squence_num += 1
        time.sleep(0.1)
    epoch +=1

