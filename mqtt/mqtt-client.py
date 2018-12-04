
# coding: utf-8

# In[8]:


import paho.mqtt.client as client
import time, subprocess, shlex
import numpy as np

HOST = "192.168.1.187"
PORT = 1883
TOPIC = "UWB"
FLAG = 0

def UWB_on_Message(client, userdata, msg):
    print( "%s %s" % (msg.topic, str(msg.payload)) )
    if(len(msg.payload)):
        speaker = int(msg.payload)
        if(speaker== FLAG):
            time.sleep(0.2)
            print("say")
            cmd = shlex.split("../dw1000_rpi_new/src/dw1000_tx")
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            print(p.communicate()[0].decode("utf-8"))
        else:
            print("hear")
            cmd = shlex.split("../dw1000_rpi_new/src/dw1000_rx_cir")
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            print(p.communicate()[0].decode("utf-8"))
    
def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + connack_string(rc))
    
def on_disconnect(client, userdata, rc):
    print("Unexpected disconnection.")

UWB_client = client.Client("Rpi" + str(FLAG))
UWB_client.on_message = UWB_on_Message
UWB_client.on_connect = on_connect
UWB_client.on_disconnect = on_disconnect
        
def UWB_client_main():
    UWB_client.connect(HOST, PORT, 60)
    UWB_client.subscribe(topic = TOPIC)
    UWB_client.loop_forever()

if __name__=='__main__':
    UWB_client_main()

