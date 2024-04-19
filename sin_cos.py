import math
def trigResylts(x):
    a = math.sin(x)
    b = 1 / math.sin(x)
    return a , b

print(trigResylts(math.pi / 2))