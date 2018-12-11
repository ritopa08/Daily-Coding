'''
Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

    10 = max(10, 5, 2)
    7 = max(5, 2, 7)
    8 = max(2, 7, 8)
    8 = max(7, 8, 7)
 '''

def eval(a,k):
  n=len(a)
  l=[]
  for i in range(n-k+1):
    x=[]
    for j in range(i,i+k):
      x.append(a[j])
    l.append(max(x))
  return l

a = [10, 5, 2, 7, 8, 7]
k = 3
print(eval(a,k))
