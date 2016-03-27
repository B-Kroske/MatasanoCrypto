import base64
from Crypto.Cipher import AES
from CryptoLib import xor, validate
import binascii

class CBC:
    def __init__(self, ECB, IV, blocksize = 16):
        self.ECB = ECB
        self.IV = IV
        self.blocksize = blocksize

    def getBlocks(self, s):
        return [s[i:i+self.blocksize] for i in range(0, len(s), self.blocksize)]

    def encrypt(self, plaintext):
        ptBlocks = self.getBlocks(plaintext)
        ciphertext = b''
        prev = self.IV
        for block in ptBlocks:
            toEnc = xor(prev, block)
            cipherBlock = self.ECB.encrypt(bytes(toEnc))
            prev = cipherBlock
            #print(cipherBlock)
            ciphertext += cipherBlock

        return ciphertext

    def decrypt(self, ciphertext):
        #Split the ciphertext into blocks
        ctBlocks = self.getBlocks(ciphertext)
        plaintext = b''
        prev = self.IV

        for block in ctBlocks:
            #Decrypt the ciphertext block and xor it with the IV/Previous block
            plainBlock = bytes(xor(prev, self.ECB.decrypt(block)))
            prev = block
            plaintext += plainBlock

        return plaintext

def main():
    key = "YELLOW SUBMARINE"
    inputFile = "assets/Set2/inputC2.txt"
    input = ''

    #Read in the file
    for line in open(inputFile,"r"):
        input += line.rstrip()
    #Un-base 64 encode the file
    ciphertext = base64.b64decode(input)

    cipher = CBC(AES.AESCipher(key, AES.MODE_ECB), bytearray([0] * 16))

    pt = cipher.decrypt(ciphertext)
    print(pt)
    ct = cipher.encrypt(pt)
    validate(ct, ciphertext)


if __name__ == '__main__':
    main()
