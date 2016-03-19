#Stores functions to simplify completing the challenges
from collections import Counter
import base64
import binascii

letterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75,
'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76,
'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29,
'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07, ' ': 0.0}

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

#Converts an ascii string to a byte array
def strToByteArr(inputStr):
    return bytearray(inputStr.encode())

#converts a hex string to a byte array
def hexToByteArr(hexStr):
    return bytearray.tohex(hexStr)

#Xors two byte arrays
#Resulting array is the same length as the first array.
def xor(arr1, key):
    len1 = len(arr1)
    keyLen = len(key)
    res = bytearray(len1)

    for i in range(0,len1):
        #print(arr1[i],key[i%keyLen],arr1[i] ^ key[i % keyLen])
        res[i] = arr1[i] ^ key[i % keyLen]
        #print(i,format('%x',res[i]))
    return res

#Finds the frequency of letters in the string and compares the top/bottom numCmp
# to the most/least common letters in english
def freqScore(string):
    counter = Counter(string.upper())
    strFreq = counter.most_common()
    length = len(string)
    score = 0

    for (x,y) in strFreq:
        try:
            score += (y / length) * letterFreq[x]
        except:
            score -= 0.1

    return score

#Brute forces a single byte xor cipher.
#Returns a tuple of the result, score, and key
def xorBruteForce1(ciphertext):
    currStr = ''
    currScore = 0
    bestStr = ''
    bestScore = 0
    key = 0

    for i in range(0,255):
        #print(bytearray({i}))
        try:
            currStr = xor(ciphertext,bytearray({i})).decode()
            currScore = freqScore(currStr)
            if(currScore > bestScore):
                bestScore = currScore
                bestStr = currStr
                key = i
        except:
            continue

    return (key, bestScore, bestStr)
