def getGcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return getGcd(b, r)


def lcm(a, b):
    return (a * b) // getGcd(a, b)


strNumbers = input("").split(" ")
NumbersArr = [int(i) for i in strNumbers]

print(lcm(NumbersArr[0], NumbersArr[1]))
