def CalcMaximumPairwise(arr):
    maxIndex1 = -1
    maxIndex2 = -1
    for index, number in enumerate(arr):
        if maxIndex1 == -1 or number > arr[maxIndex1]:
            maxIndex1 = index

    for index, number in enumerate(arr):
        if index != maxIndex1 and (maxIndex2 == -1 or number > arr[maxIndex2]):
            maxIndex2 = index

    return arr[maxIndex2] * arr[maxIndex1]


numberOfElements = input("")

numInput = input("")

stringArr = numInput.split(" ")


numArr = [int(numeric_string) for numeric_string in stringArr]


print(CalcMaximumPairwise(numArr))
