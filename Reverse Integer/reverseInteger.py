def reverseInteger(x):
    sign = -1 if x < 0 else 1
    x = x * sign
    
    res = 0
    while(x):
        res = res * 10 + x % 10
        x = x//10
    res = res * sign
    
    if res > 2**31 - 1 or res < -2**31:
        return 0
    else:
        return res
    
print(reverseInteger(-321))
    