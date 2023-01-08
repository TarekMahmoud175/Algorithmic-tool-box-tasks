PISANO = 60  # 1
 
 
def solution(number):
    if number < 2:
        return number
 
    number %= PISANO
 
    results = [1, 1]
    for _ in range(number):  # 2
        results.append((results[-1] + results[-2]) % 10)  # 3
 
    return (results[-1] - 1) % 10  # 4


strInput = input("")
number = int(strInput)

print(solution(number))
