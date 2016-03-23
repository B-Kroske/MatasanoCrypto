from CryptoLib import everyNth, validate
from collections import Counter
import binascii

def calcScore(array):
    counter = Counter(array)
    arrFreq = counter.most_common()
    res = 0
    for i in range(0,3):
        res += arrFreq[i][1]
    return res



def main():
    ans = "d880619740a8a19b7840a8a31c810a3d08649af70dc06f4fd5d2d69c744cd283e2dd052f6b641dbf9d11b0348542bb5708649af70dc06f4fd5d2d69c744cd2839475c9dfdbc1d46597949d9c7e82bf5a08649af70dc06f4fd5d2d69c744cd28397a93eab8d6aecd566489154789a6b0308649af70dc06f4fd5d2d69c744cd283d403180c98c8f6db1f2a3f9c4040deb0ab51b29933f2c123c58386b06fba186a"

    #Read in the entire file and concatenate it to a string.
    inputFile = "assets/Set1/inputC8.txt"
    posCipher = None

    switch = True

    lineScore = 0
    cipherLine = None
    bestScore = 0

    #Determine how many characters on each line encrypted with
    # the same key are the same.
    #The one with the highest score is likely encrypted text
    # as opposed to random hex
    for line in open(inputFile,"r"):
        lineScore = 0
        switch = not switch
        posCipher = line.rstrip()
        posCipher = binascii.unhexlify(posCipher)
        #Repeat for every block of bytes that would be encoded
        # with the same key.
        for i in range(0,16):
            lineScore += calcScore(everyNth(posCipher, 16))
        if (lineScore > bestScore):
            cipherLine = line
            bestScore = lineScore

    print(cipherLine)

if __name__ == "__main__":
    main()
