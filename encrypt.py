import keystream_gen
import os
import glob

def getNewKeyByte(register19, register22, register23):
    newKeyByte = 0
    for i in range(8):
        newKeyBit, register19, register22, register23 = keystream_gen.generateNewKeyBit(register19, register22, register23)
        newKeyByte = newKeyByte * 2 + newKeyBit
    return newKeyByte

if __name__ == '__main__':
    fileFormat = glob.glob("input.*")[0].split('.')[1]
    inFileName = "input." + fileFormat
    file = open(inFileName, "rb")

    outFileName = "input." + fileFormat + ".enc"
    outFile = open(outFileName, "wb")

    key = keystream_gen.getKey()
    register19, register22, register23 = keystream_gen.loadRegisters(key)

    while True:
        plainText = file.read(1)
        if not plainText: break
        encryptedNewByte = list(plainText)[0] ^ getNewKeyByte(register19, register22, register23)
        outFile.write(encryptedNewByte.to_bytes(1, 'little'))

    file.close()
    outFile.close()