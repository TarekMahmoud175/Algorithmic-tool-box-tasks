def findMaximumCoin(money, coinsArr):
    maximum = 0
    for i in coinsArr:
        if(i > maximum and i <= money):
            maximum = i
    return maximum


def moneyChange(money, coins):
    numberOfcoins = 0
    if money == 0 or len(coins) == 0:
        return 0
    else:
        while(money > 0):
            maxCoin = findMaximumCoin(money, coins)
            money = money - maxCoin
            if(money < maxCoin):
                coins.remove(maxCoin)
            numberOfcoins += 1
    return numberOfcoins


money = int(input())

# coinsStrArr = input().split(" ")

# coinsArr = [int(i) for i in coinsStrArr]


print(moneyChange(money, [10, 5, 1]))
