#!/usr/bin/env python
# coding: utf-8

import time

result= time.localtime()

print(result)

while True:
    result=time.localtime()
    if result.tm_hour==16 and result.tm_min==11:
        print("Hey! Dude It's Time to Wake-up")
        break
