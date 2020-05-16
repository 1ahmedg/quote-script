#1.0

from q_dic import dic
from random import randint
from os.path import getsize

def check(x,file):
    infile = open(file,"r",encoding='utf-8')
    temp = [line.strip() for line in infile.readlines()]
    if x in temp:
        return True
    else:
        return False

def number(): # generates random number(s) 
    return randint(0,len(dic))

def randomq(): # random quote
    return dic[number()-1]

def resetq(): # reset function
    x = input("All the quotes have been posted at least once\nTruncate file?(yes/no)\n")
    if x == "yes" or x == "Yes": # if answer is yes, yike the contents
        file = open('cache.txt','w')
        file.truncate()
        return "File size = " + str(getsize('cache.txt'))
    else:
        return "No action taken, see ya!"
        

def naval_quote():
    infile = open('cache.txt','a+') # open file for writing
    x = randomq()
    try:
        if check(x,'cache.txt') == False: # if not found, write in cache and return it
            infile.write(f"{x}\n")
            return x
        elif check(x,'cache.txt') == True: # if found, recall function
            return naval_quote()
    except RecursionError: 
# return "All quotes have been posted at least once, truncate cache"
        return resetq() # call reset function to determine the future

    infile.close()
