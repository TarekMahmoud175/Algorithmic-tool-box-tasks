def sumOfTwoDigits():
    numbers = input("")
    numbersArr = numbers.split(" ")
    return int(numbersArr[0]) + int(numbersArr[1])

print(sumOfTwoDigits())