def merge(nums1,m,nums2,n):
  i = m - 1
  j = n - 1
  last = m + n -1
  while(j >= 0):
    if i >=0 and nums1[i] > nums2[j]:
      nums1[last] = nums1[i]
      i = i - 1
    else:
      nums1[last] = nums2[j]
      j = j - 1
    last = last - 1
