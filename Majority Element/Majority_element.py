#Hashmap approach
from collections import Counter
def majrotiyElement(nums):
    c = Counter(nums)
    l = len(nums)//2
    for keys, values in c.items():
        if(values>l):
            return keys
    return None

#Moore Voting Algorithm

def majorityElement(nums):
    count = 0 
    candidate = 0

    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count +=1
        else:
            count -=1
    return candidate


