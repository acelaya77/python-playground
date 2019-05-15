#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 16:05:53 2018

@author: anthonycelaya
"""

with open('/etc/hosts') as hosts:
    
    count = 0
    for line in hosts:
        count = count + 1
        #print(format(count, '02d') + ' ' + line.rstrip())
        print('{0:02d}: {1}'.format(count,line.rstrip()))
        
    hosts_content = hosts.read()
#print("Hosts closed? {}".format(hosts.closed))

#print(hosts_content)

