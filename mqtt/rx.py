
# coding: utf-8

# In[ ]:


import subprocess, shlex
cmd = shlex.split("/home/pi/dw1000_rpi_new/src/dw1000_rx_cir")
p = subprocess.Popen(cmd, stdout=subprocess.PIPE, timeput=2)
print(p.communicate()[0].decode("utf-8"))
