def sumOfTwoDigits():
    numbers = input("Please enter numbers")
    numbersArr = numbers.split(" ")
    return int(numbersArr[0]) + int(numbersArr[1])

print(sumOfTwoDigits())