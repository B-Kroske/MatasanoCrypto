import binascii
import CryptoLib

def main():
    ans = '746865206b696420646f6e277420706c6179'
    hexStr1 = '1c0111001f010100061a024b53535009181c'
    hexStr2 = '686974207468652062756c6c277320657965'
    byteArr1 = bytearray.fromhex(hexStr1)
    byteArr2 = bytearray.fromhex(hexStr2)

    #The byte array we will build and a variable for its hex string
    byteArr3 = bytearray()
    res = ''

    #Could also use CryptoLib.xor(byteArr1,byteArr2)
    for x,y in zip(byteArr1,byteArr2):
        byteArr3.append(x ^ y)

    res = binascii.hexlify(byteArr3).decode()
    print(byteArr3.decode())
    print(res)
    CryptoLib.validate(res, ans)

if __name__ == "__main__":
    main()
