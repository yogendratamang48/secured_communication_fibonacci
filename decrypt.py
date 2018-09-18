import json
import encrypt
FILE_TO_DECODE = 'message.txt'

def start_decript(rawSecurityCode):
    asciiLetters = encrypt.getAsciiLetters()
    encoded_hexes = eval(open(FILE_TO_DECODE, 'r').read())
    if len(rawSecurityCode)==1 and rawSecurityCode[0] in asciiLetters:
        _decimals = [int(_hex, 16) for _hex in encoded_hexes]
        decoded_message = encrypt.getDecodedMessage(rawSecurityCode, _decimals)
        print("Decoding...")
        # print(decoded_message)
        return decoded_message
    else:
        print("Wrong Security Key")

if __name__=='__main__':
    rawSecurityCode = input("Enter Security Code: ")
    mess = start_decript(rawSecurityCode)
    print(mess)
    # Single Character Validation

    # Reading file
    