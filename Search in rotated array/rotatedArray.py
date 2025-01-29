def search(nums,target):
    low = 0 
    high = len(nums) - 1
    
    while low <= high:
        mid = low + (high-low)//2
        if (nums[mid]==target):
            return mid
        
        #left sorted
        if nums[low] <= nums[mid]:
            if nums[low]<=target<=nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
                
        #right sorted
        else:
            if nums[mid]<=target<= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

print(search([4,5,6,7,0,1,2],7))