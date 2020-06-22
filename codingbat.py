def sum67(nums):
  a=0
  b=0
  count =0
  count2=0
  while count<len(nums):
    if nums[count]==6:
      a=count
      while nums[count]!=7:
        count+=1
        b=count
        
      del nums[a:b+1]
      count=0
          
    count += 1  
  
  for num in nums:
    count2=count2+num
  return count2