def getGcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return getGcd(b, r)


strNumbers = input("")
strNumberArr = strNumbers.split(" ")
NumberArr = [int(i) for i in strNumberArr]

print(getGcd(NumberArr[0], NumberArr[1]))
