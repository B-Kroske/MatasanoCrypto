from CryptoLib import xor, strToByteArr, xorBruteForce1, validate
import base64

def calcHamming(arr1, arr2):
    numBits = 0
    resArr = xor(arr1,arr2)
    for j in range(0,len(arr1)):
        numBits += bin(resArr[j]).count('1')
    return numBits

def avgHamming(array, hamLen, hamCount = 1):
    start = 0
    end = hamLen
    numBits = 0

    currArr = []
    nextArr = []
    resArr = []

    for i in range(0,hamCount):
        currArr = array[start:end]
        start = end
        end += hamLen
        nextArr = array[start:end]
        numBits += calcHamming(currArr,nextArr)
        #print(hamLen,"-",numBits)

    return float(numBits) / hamCount

#Returns a byte array consisting of every nth character.
def everyNth(array,n,start = 0):
    resLen = int(len(array) / n)
    resArr = bytearray(resLen)

    for i in range(0, resLen):
        resArr[i] = array[(start + (n * i))]

    return resArr

def main():
    inputFile = "assets/Set1/inputC6.txt"

    inputStr = ''
    newHam = 0
    bestHam = 10000
    keyLen = 0
    key = None
    res = None


    #Read in the entire file and concatenate it to a string.
    for line in open(inputFile,"r"):
        inputStr += line.rstrip()

    #Decode the input from base 64 and convert it to a byte string.
    decodedStr = bytearray(base64.b64decode(inputStr))

    #print(inputStr)
    #print(base64.b64decode(inputStr))
    for i in range(1,40):
        newHam = avgHamming(decodedStr,i, 10) / i
        #print(i,"hamming dist",newHam)
        if(newHam < bestHam):
            bestHam = newHam
            keyLen = i

    #Create the array that will store the key
    key = bytearray(keyLen)

    for i in range(0,keyLen):
        encChunk = everyNth(decodedStr,keyLen, i)
        (k,d,r) = xorBruteForce1(encChunk)
        key[i] = k

    print("Key:", key.decode())
    print("\n\nDeciphered text:")
    res = xor(decodedStr,key)
    #print(res)
    print(res.decode("ascii"))


if __name__ == "__main__":
    main()
