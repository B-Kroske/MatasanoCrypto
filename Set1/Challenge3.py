import binascii
import CryptoLib

def main():
    ans = "Cooking MC's like a pound of bacon"

    inputStr = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    inputArr = bytearray.fromhex(inputStr)
    currStr = ''
    currScore = 0
    bestStr = ''
    bestScore = 0

    for i in range(0,256):
        #print(bytearray({i}))
        try:
            currStr = CryptoLib.xor(inputArr,bytearray({i})).decode()
            currScore = CryptoLib.freqScore(currStr)
            if(currScore > bestScore):
                bestScore = currScore
                bestStr = currStr
        except:
            continue

    print(bestStr)
    CryptoLib.validate(bestStr, ans)

if __name__ == "__main__":
    main()
