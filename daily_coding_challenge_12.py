''' 
Given an array of integers, find the first missing positive integer in linear time and constant space.
 In other words, find the lowest positive integer that does not exist in the array. 
 The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''




def missing_no(a,n):
  x=1
  for i in range(n):
    if(a[i]==x):
      x=x+1
  return(x)
  
  
  

a= [1, 2, 0]
n=len(a)
print(missing_no(a,n))
