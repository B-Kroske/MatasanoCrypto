import base64
from Crypto.Cipher import AES
from CryptoLib import strToByteArr

def main():

    #Read in the entire file and concatenate it to a string.
    inputFile = "assets/Set1/inputC7.txt"
    x=""
    for line in open(inputFile,"r"):
        x += line.rstrip()

    ciphertext = base64.b64decode(x)
    key = "YELLOW SUBMARINE".encode()

    cipher = AES.AESCipher(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    print(plaintext.decode())

if __name__ == "__main__":
    main()
