from CryptoLib import strToByteArr

#Pads the given arrayj out to padLen bytes
def padStr(arr, padLen, padChar = 4):
    for i in range(len(arr), padLen):
        arr.append(padChar)
    return arr

def main():
    key = "YELLOW SUBMARINE"
    blockSize = 20
    padded = padStr(strToByteArr(key), 20)
    print(padded)

if __name__ == "__main__":
    main()
