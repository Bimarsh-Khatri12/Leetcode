def addDigits(digits):
    if digits == 0:
        return 0
    if digits % 9 == 0:
        return 9
    else:
        return digits % 9

print(addDigits(79))