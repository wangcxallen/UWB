#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 19:28:06 2019

@author: wangchenxi
"""

import sys

flag = sys.argv[1]

def main():
    file = open("flag.txt", "w")
    file.write("%s" % flag)
    file.close()

if __name__ == "__main__":  
    main() 