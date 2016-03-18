#Stores functions to simplify completing the challenges

import base64

def validate(guess, ans, isVerbose = False):
    try:
        assert(guess == ans)
        print("Valid Answer")
    except:
        print("Invalid Answer")

        if(isVerbose != False):
            print('' + str(guess) + " != " + str(ans))



#Takes a hex string or a byte array/string to convert to base 64
def toBase64(val):
    if(type(val).__name__ == 'str'):
        return base64.b64encode(bytes.fromhex(val))
    elif(type(val).__name__ == 'bytearray' or
        type(val).__name__ == 'bytes'):
        return base64.b64encode(val)

#Xors two byte arrays
#Resulting array is the same length as the first array.
def xor(arr1, arr2):
    len1 = len(arr1)
    len2 = len(arr2)
    res = bytearray()

    for i in range(0,len1):
        res.append(arr1[i] ^ arr2[i % len2])
    print(res)
