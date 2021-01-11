 # -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 09:52:24 2021

@author: SSR
"""

def myfunction():
  #  print("protocol")
  #  print("1]add a new calender event",'\n',"2]remove a calender event","\n","3]update the calender","\n","4]get the events for specified time/time range") 
     string = input("enter calender event")
     list1 = string.split()
     if list1[1] == "add" :
         add(list1)
     elif list1[1] == "remove":
         remove(list1)
     elif list1[1] == "update":
         update(list1)
     elif list1[1] == "get":
         get(list1)
    
def add(list1):
    with open("worksheet1.txt","a") as f:
        f.write("\n")
        for i in list1:
            f.write(i)
            f.write("\t")
        f.truncate()
    choice = input("wanna do any other calender changes activity [yes/no]")
    if choice == "yes":
        myfunction()

def remove(list1):
    print(list1)
    with open("worksheet1.txt","r") as f: 
            if list1[2]  not in line:
                    f.write(line)
    choice = input("wanna do any other calender changes activity [yes/no]")
    if choice == "yes":
        myfunction()
        
def update(list1):
    with open("worksheet1.txt","r") as f:
        file = f.readlines()
    with open("worksheet1.txt","w") as f:
        for line in file:
              if list1[0] in line:
                s = line.split()
                line = line.replace(s[2],list1[2])
                line = line.replace(s[3],list1[3])
                line = line.replace(s[5],list1[5])
                line = line.replace(s[4],list1[4])
            f.write(line)
        f.truncate()
    choice = input("wanna do any other calender changes activity [yes/no]")
    if choice == "yes":
        myfunction()
        
def get(list1):
    with open("worksheet1.txt","r") as f:
        file = f.readlines()
        for line in file:
            if list1[2] in line:
                    list2 = line.split()
                    print(list2[5])
    choice = input("wanna do any other calender changes activity [yes/no]")
    if choice == "yes":
        myfunction()
        
myfunction()