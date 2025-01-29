def twoSum(nums, target):
  hashmap = {}
  for index , value in enumerate(nums):
    diff = target - value
    if diff in hashmap:
      return hashmap[diff], index
    else:
      hashmap[value] = index
      
