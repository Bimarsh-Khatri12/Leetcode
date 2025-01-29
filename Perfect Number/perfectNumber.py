import math

def perfectNumber(num):
    if num == 1:
        return False
    
    sum = 1
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            sum = sum + i + num//i
    return num == sum

print(perfectNumber(28))
