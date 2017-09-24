# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 00:14:20 2017

@author: deepak
"""

x=0
epsillon=1
numguess=0
high=100
low=1
ans=(high+low)/2
while abs(ans-x)>=epsillon:
    print("Ans"+ str(ans))
    numguess += 1
    k=2
    k=input("""Enter 'h' to indicate the guess is too high. Enter 'l' to indicate\      the guess is too low.Enter 'c' to indicate I guess correctly""")
    if k=="l":
        low = ans
    elif k=="h":
        high = ans
    else:
       print("Didn't understand input")
    ans=(high+low)/2
    print("Ans is"+ str(ans))
    l
    
    
    
    