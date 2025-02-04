def checkArray(nums):
    breakPoint = 0
    for i in range(1,len(nums)):
        if nums[i-1] > nums[i]:
            breakPoint = breakPoint + 1
    if nums[len(nums)-1] > nums[0]:
        breakPoint = breakPoint + 1
    return breakPoint<=1

print(checkArray([2,1,3,4]))