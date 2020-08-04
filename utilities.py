#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 19:03:09 2020

@author: Nick
"""

import re 

def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)

def refineMSG(string):
    returnStr = ''
    for char in string:
        if(char != "<"):
            returnStr = returnStr + char 
        else: 
            break
  
    return returnStr
            


def get_sender(unparsed_data):
    for i in range(len('Return-Path: <'),len(unparsed_data)):
        smtpmatch = unparsed_data[i-len('Return-Path: <')+1:i+1]
        if smtpmatch == "Return-Path: <":
            break;
    email_address =""
    i=i+1
    while(unparsed_data[i]!=">"):
        email_address = email_address+unparsed_data[i]
        i=i+1
    return email_address
