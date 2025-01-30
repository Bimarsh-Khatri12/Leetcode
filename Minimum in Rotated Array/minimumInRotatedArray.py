def minimumRotatedArray(nums):
    low = 0
    high = len(nums) - 1
    
    while low < high:
        mid = low + (high - low)//2
        
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid
    return nums[low]

print(minimumRotatedArray([1,0,1,1,1]))