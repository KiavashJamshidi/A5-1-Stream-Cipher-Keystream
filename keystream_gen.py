def isBinary(string) :
 
    p = set(string)
 
    s = {'0', '1'}

    if s == p or p == {'0'} or p == {'1'}:
        return True
    else :
        return False
    
def getKey():
    while True:
        key = input("Enter your key: ").strip()
        if len(key) != 64: 
            print("The length of key is not 64! please try again!")
            continue
        if not isBinary(key):
            print("The key is not binary! please try again!")
            continue
        return key

def loadRegisters(key):
    register19, register22, register23 = [], [], []

    for i in range(19):
        register19.append(int(key[i]))
    for i in range(19,41):
        register22.append(int(key[i]))
    for i in range(41,64):
        register23.append(int(key[i]))
    return register19, register22, register23

def major(x, y, z):
    if x + y + z > 1:
        return 1
    else:
        return 0
    
def regOutput(register, maj, howManyBit):
    if howManyBit == 19:
        if register[8] == maj:
            newBit = register[18] ^ register[17] ^ register[16] ^ register[13]
            outBit = register[-1]
            register = [newBit] + register[0:18]
            return outBit, register
        else:
            return register[-1], register

    elif howManyBit == 22:
        if register[10] == maj:
            newBit = register[21] ^ register[20]
            outBit = register[-1]
            register = [newBit] + register[0:21]
            return outBit, register
        else:
            return register[-1], register

    elif howManyBit == 23:
        if register[10] == maj:
            newBit = register[22] ^ register[21] ^ register[20] ^ register[7]
            outBit = register[-1]
            register = [newBit] + register[0:22]
            return outBit, register
        else:
            return register[-1], register

def generateNewKeyBit(register19, register22, register23):
    maj = major(register19[8], register22[10], register23[10])
    reg19OutBit, register19 = regOutput(register19, maj, 19)
    reg22OutBit, register22 = regOutput(register22, maj, 22)
    reg23OutBit, register23 = regOutput(register23, maj, 23)
    newBit = reg19OutBit ^ reg22OutBit ^ reg23OutBit
    return newBit, register19, register22, register23
