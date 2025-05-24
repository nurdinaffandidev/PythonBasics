def find_max(numbers):
    maxNum = numbers[0]
    for number in numbers:
        maxNum = max(maxNum, number)
    return maxNum