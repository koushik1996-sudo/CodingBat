def has22(nums):
  count1=0
  count=0
  while count<(len(nums)-1):
    if nums[count]==2 and nums[count+1]==2:
      return True
    
    count=count+1
  return False