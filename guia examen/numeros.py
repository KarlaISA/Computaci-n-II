from Stack import Stack

def divideByN(decNumber,base):
    remstack = Stack()

    while decNumber >0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString
print(divideByN(42,2))
