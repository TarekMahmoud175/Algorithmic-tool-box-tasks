# def FebFunc(n):
#     arr = [0, 1]
#     if (n < 2):
#         return arr[n]
#     for i in range(2, n+1):
#         answer = arr[i - 1] + arr[i - 2]
#         arr.append(answer)

#     return arr[n]


# strNumber = input("")
# number = int(strNumber)
# strNumberOutput = str(FebFunc(number))
# print(strNumberOutput[-1])

def fib_last_digit(n):
    if n < 2: return n
    else:
        a, b = 0, 1
        for i in range(1,n):
            a, b = b, (a+b) % 10
        print(b)

n = int(input())
fib_last_digit(n)