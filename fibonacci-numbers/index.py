# def febFunc(n):
#     if (n < 2): return n
#     else: return febFunc(n - 1) + febFunc(n - 2)


def goodFebFunc(n):
    arr = [0, 1]
    if (n < 2):
        return arr[n]
    for i in range(2, n+1):
        answer = arr[i - 1] + arr[i - 2]
        arr.append(answer)

    return arr[n]


strNumber = input("")
number = int(strNumber)
print(goodFebFunc(number))
