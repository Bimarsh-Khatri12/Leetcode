def search(nums,target):
    low = 0 
    high = len(nums) - 1
    
    while low <= high:
        mid = low + (high-low)//2
        if (nums[mid]==target):
            return True
        
        #left sorted
        elif nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
                
        #right sorted
        elif nums[low] >= nums[mid]:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            low = low + 1
    
    return False

print(search([1,0,1,1,1],0))