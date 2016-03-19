from CryptoLib import strToByteArr, xor, validate
import binascii
def main():
    ans =   "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272"
    ans +=  "a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    ans = bytearray.fromhex(ans)

    inputStr =  "Burning 'em, if you ain't quick and nimble\n"
    inputStr += "I go crazy when I hear a cymbal"

    key = "ICE"

    inputArr = bytearray(inputStr.encode())

    keyArr = bytearray(key.encode())

    res = xor(inputArr,keyArr)
    print(binascii.hexlify(res))
    validate(res, ans)

if __name__ == "__main__":
    main()
