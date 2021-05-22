# -*- coding: utf-8 -*-
"""
Created on Tue May 11 21:03:43 2021

@author: Mukul
"""

#string
mystring= 'How are you ?'
mystring[2]
mystring.split(" ")[1]  #ordered
mystring[1]="h" #immutable

#list
mylist=["AAA",123,"BBB"]
mylist[1]         #ordered
mylist[2]="Devi"  #mutable

#tuple
mytuple=("AAA",123,"BBB")
mytuple[1]       #ordered
mytuple[2]="Devi"      #immutable

#sets
set1=set([1,1,2,1,2,1,1,3,3,3])  #unordered #immutable

#dictionary
Player_Location={"Bangalore":["Dravid","Srinath","Kumble"],"New Delhi":["Sehwag","Virat"]}
Player_Location["Bangalore"]
Player_Location["Bangalore"][1]
