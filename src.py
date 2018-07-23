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

def getEncodedDecimals(keys, messages):
    '''
    returns encoded decimals from keys and message pairs
    '''
    encodedDecimals = []
    for key, message in zip(keys, messages):
        key_ord = ord(key)
        message_ord = ord(message)
        decimal = 3*key_ord+message_ord
        encodedDecimals.append(decimal)
    return encodedDecimals

def getDecodedMessage(securityKey, encodedDecimals):
    '''
    returns decoded message from security key and encoded decimals
    1. get keys
    2. get ascii_values of keys
    3. get decoded decimals = encodedDecimal-3*ord_key
    4. get character from decoded decimal
    '''
    message_length = len(encodedDecimals)
    # 1. get keys
    keys = getKeys(securityKey, message_length)

    # 2. get ascii_values of keys
    ord_keys = [ord(key) for key in keys]

    # 3. get decoded decimals = encodedDecimal-3*ord_key

    decodedDecimals = [0]*message_length
    for i in range(message_length):
        decodedDecimals[i] = encodedDecimals[i] - 3*ord_keys[i]

    # 4. get character from decoded decimal
    decodedCharacters = [chr(decimal) for decimal in decodedDecimals]
    decodedMessage = ''.join(decodedCharacters)

    return decodedMessage

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
        messages = list(message)
        print("Keys: ")
        print(keys)

        encodedDecimals = getEncodedDecimals(keys, messages)
        print("Encoded Decimals: ")
        print(encodedDecimals)

        print("Decoding...")
        decoded_message = getDecodedMessage(rawSecurityCode, encodedDecimals)
        print(decoded_message)


    else:
        print("Wrong Character for code")

    
