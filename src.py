#! /usr/bin/env python
# src.py 

import string
from itertools import cycle
import pdb

def getFibonacciNumbers(limit):
    '''
    returns "limit" number of fibonacci numbers
    '''
    if limit == 1:
        return [1]
    if limit == 2:
        return [1, 2]
    
    fibonacciNumbers = [1, 2]
    i=2
    while i<(limit):
        toAdd = fibonacciNumbers[i-1]+fibonacciNumbers[i-2]
        fibonacciNumbers.append(toAdd)
        i +=1
    return fibonacciNumbers


def getKeys(securityCode, messageLength):
    '''
    returns security code, round robin fashion. 
    '''
    keys = [0]*messageLength
    letters = getAsciiLetters()
    cycleLetters = cycle(letters)
    securityCodeIndex = letters.index(securityCode)
    fibos = getFibonacciNumbers(messageLength)
    # Rotate cycle to securityCodeIndex

    rangeToTake = max(securityCodeIndex-1, 0)+1

    for i in range(rangeToTake):
        next(cycleLetters)
    # pdb.set_trace()
    # Iterate and collect as per fibos
    for i, fibo in enumerate(fibos):
        if i == 0:
            keys[i] = next(cycleLetters)
            continue
        j = fibos[i]-fibos[i-1] 
        for k in range(j):
            keys[i] = next(cycleLetters)

    return keys


def getAsciiLetters():
    '''
    returns lower case letters as list cyclic
    '''
    return list(string.ascii_lowercase)

if __name__=='__main__':
    message=input("Enter your text: ")
    print(message)
    rawSecurityCode = input("Enter Security Code: ")
    # Single Character Validation
    asciiLetters = getAsciiLetters()
    if len(rawSecurityCode)==1 and rawSecurityCode[0] in asciiLetters:
        print("Security Code: {}".format(rawSecurityCode))
        keys = getKeys(rawSecurityCode, len(message))
        print(keys)

    else:
        print("Wrong Character for code")

    