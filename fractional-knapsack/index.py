def findMaxLootfraction(fractions):
    max = 0
    for i in fractions:
        if i > max:
            max = i

    return fractions.index(max)


def calcMinimum(x, y):
    if x <= y:
        return x
    else:
        return y


def maximizeLoot(W, Weights, Costs):
    fractionArr = []
    for x in range(len(Weights)):
        fractionArr.append(Costs[x]/Weights[x])
        
    if W == 0 or len(Weights) == 0:
        return 0
    
    else:
        maxIndex = findMaxLootfraction(fractionArr)
        amount = calcMinimum(Weights[maxIndex], W)
        value = (amount/Weights[maxIndex]) * Costs[maxIndex]
        newBagWieght = W - amount
        Weights.pop(maxIndex)
        Costs.pop(maxIndex)
        return value + maximizeLoot(newBagWieght, Weights, Costs)


n, bagWeight = map(int, input().split(" "))
Wieghts = []
Costs = []
for i in range(n):
    value, weight = map(int, input().split())
    Wieghts.append(weight)
    Costs.append(value)


print(maximizeLoot(bagWeight, Wieghts, Costs))

