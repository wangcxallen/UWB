#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 17:49:15 2019

@author: wangchenxi
"""

import paramiko, sys  

def main():  
      
    server = ['192.168.1.209',
              '192.168.1.200',
              '192.168.1.200',
              '192.168.1.200',
              '192.168.1.200']
    username = 'pi'  
    password = 'raspberry'
    misconnection = []
    
    for hostname in server:
        print(hostname)
        rpi = paramiko.SSHClient()  
        rpi.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            rpi.connect(hostname=hostname, username=username, password=password, timeout=5)
            ssh_stdin, ssh_stdout, ssh_stderr = rpi.exec_command("python /home/pi/UWB/mqtt/host.py")
            # This function just pass throught the command. It doesn't wait for it to end.
        except:
            misconnection.append(hostname)
            sys.exit(0)
    
    if misconnection!=[]:
        print("Misconnection occurs:")
        for hostname in misconnection:
            print(hostname)
    
if __name__ == "__main__":  
    main()  