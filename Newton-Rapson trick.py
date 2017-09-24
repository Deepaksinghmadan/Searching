# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 01:11:52 2017

@author: deepak
"""

epsillon=0.01
x=104
guess=x/2
numguess=0
while abs(guess*guess-x) >=epsillon:
    numguess += 1
    guess=guess-(((guess**2)-x)/(2*guess))
print("number of guess req=" + str(numguess)+ " and guess is " + str(guess))


