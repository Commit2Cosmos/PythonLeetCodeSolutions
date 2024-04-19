def isValidSubsequence(array, sequence):
    j = 0
    for i in array:
        if i == sequence[j]:
            j += 1
        if j == len(sequence):
            return True
    return False



x = [1, 2, 3, 4, 5]
y = [2, 1]
print(isValidSubsequence(x, y))