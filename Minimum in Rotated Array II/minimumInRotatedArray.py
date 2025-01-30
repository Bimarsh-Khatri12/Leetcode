def minimumRotatedArray(nums):
    low = 0
    high = len(nums) - 1
    
    while low < high:
        mid = low + (high - low)//2
        if nums[mid] == nums[high]:
            high = high - 1
        elif nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid
    return nums[low]

print(minimumRotatedArray([3,3,1,3]))