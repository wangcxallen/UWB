
# coding: utf-8

# In[ ]:


import paho.mqtt.publish as publish
import time
import numpy as np

HOST = "192.168.1.199"
PORT = 1884

epoch = 0
squence_num = 0
while(epoch<1000):
    for i in np.arange(4):
        print("RPI %i speaks..." % i)
        print("MSG %i" % squence_num)
        print("-"*30)
        publish.single("UWB", "%i%i"% (i, squence_num), hostname=HOST, port=PORT)
        squence_num += 1
        time.sleep(10)
    epoch +=1

