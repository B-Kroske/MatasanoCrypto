import base64
import CryptoLib

def main():
    ans = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    hexStr = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    byteArr = bytes.fromhex(hexStr)

    encodedStr = base64.b64encode(byteArr)

    print(encodedStr)
    CryptoLib.validate(encodedStr, ans)

if __name__ == "__main__":
    main()
