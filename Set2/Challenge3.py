from CryptoLib import strToByteArr, CBC, pkcs7, everyNth
from random import randint
from Crypto.Cipher import AES
from collections import Counter
'''
#Pads the given array out to padLen bytes.
# isSuffix controls whether the bytes are appended or prefixed
# isRand controls whether the bytes are randomized
# You can pass in a byte array and it will be appended to the
#   array repeatedly until the array is long enough.
def padStr(arr, padLen, isSuffix = True, isRand = True, pad = bytearray({0})):
    newArr = None
    arrLen = len(arr)
    padSize = padLen - len(arr)
    #Pad the array with 0's
    if(isSuffix):
        newArr = arr
        newArr.extend(bytearray(padSize))
    else:
        newArr = bytearray(padLen - len(arr))
        newArr.extend(arr)

    #Pad the array with random values if necessary
    if(isRand):
        print(padSize)
        if(isSuffix):
            for i in range(padSize):
                arr[arrLen + i] = randint(0,255)
        else:
            for i in range(padSize):
                newArr[i] = randint(0,255)
    else:
        #Append with the padding values, repeated as necessary
        if(isSuffix):
            for i in range(padSize):
                newArr[arrLen + i] = pad[i % padSize]
        else:
            for i in range(padSize):
                newArr[i] = pad[i % padSize]

    return newArr
'''
def genData(count = 16):
    ret = bytearray(count)
    for i in range(count):
        ret[i] = randint(0,255)
    return ret

def randPad(string):
    pre = randint(5,10)
    post = randint(5,10)
    #print("Prepending:",pre,"\nPost:",post)
    return genData(pre) + bytearray(string.encode()) + genData(post)

def randomEnc(pt):
    #Generate the key
    key = bytes(genData());
    #Pad the string
    padStr = randPad(pt)

    ct = None

    #Choose encryption method
    if(randint(1,2) == 1):
        #Set up the cipher
        cipher = AES.AESCipher(key, AES.MODE_ECB)
        #Pad the string using pkcs7
        padStr = pkcs7(padStr)

        ct = cipher.encrypt(bytes(padStr))#"pt.decode('latin-1')")
        #What encryption method was used?
        #print("EBC")
        method = "EBC"
    else:
        cipher = CBC(AES.AESCipher(key, AES.MODE_ECB), genData())
        ct = cipher.encrypt(padStr)
        #print("CBC")
        method = "CBC"

    return (ct, method)

def isECB(ct):
    arr = bytearray(ct)
    count = None
    score = 0
    for i in range(16):
        nthStr = everyNth(arr, 16, i)
        count = Counter(bytes(nthStr))
        common = count.most_common()
        score += common[0][1]

    #print("Score =", score)
    #print("len =", len(ct))
    if(score > len(ct) / 14):
        return True
    else:
        return False

#Expects the CT as a bytes string
def encryptionOracle(ct):
    if(isECB(ct)):
        #print("I'm sensing a book of electronic codes.")
        return "EBC"
    else:
        #print("I see chains of blocks")
        return "CBC"

def main():

    correct = 0
    for i in range (0, 100):
        encStr = randomEnc("So come on, everybody and sing this song Say -- Play that funky music Say, go white boy, go white boy go play that funky music Go white boy, go white boy, go Lay down and boogie and play that funky music till you die. Play that funky music Come on, Come on, let me hear Play that funky music white boy you say it, say it Play that funky music A little louder now Play that funky music, white boy Come on, Come on, Come on Play that funky music")
        guess = encryptionOracle(encStr[0])
        if(guess == encStr[1]):
            correct += 1

    print(correct);

if __name__ == "__main__":
    main()
