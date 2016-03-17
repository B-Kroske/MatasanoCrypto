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



#Takes a hex string or binary array and converts it to base 64
def toBase64(val):
    print(type(val).__name__)
    if(type(val).__name__ == 'str'):
        return base64.b64encode(bytes.fromhex(val))
    elif(type(val).__name__ == 'bytes'):
        return base64.b64encode(val)
