import binascii
import CryptoLib

def main():
    ans = "Now that the party is jumping\n"

    inputFile = "assets/Set1/inputC4.txt"

    inputArr = bytearray()
    key = 0
    score = 0
    val = ''
    topScore = 0
    res = ''

    #Read in the file line by line
    for line in open(inputFile, 'r'):
        inputArr = bytearray.fromhex(line.rstrip())
        (key,score,val) = CryptoLib.xorBruteForce1(inputArr)

        #Keep track of the best result
        if(score > topScore):
            topScore = score
            res = val

    print(res)
    CryptoLib.validate(res, ans)

if __name__ == "__main__":
    main()
