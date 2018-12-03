1. 
'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

'''

def match_list(a,k):
  l=[]
  for i in range(len(a)):
    for j in range(i+1,len(a)):
      s=a[i]+a[j]
      l.append(s)
  l=set(l)
  if k in (l):
    print("true")
  else:
    print("false")        


a=[10, 15, 3, 7]
k=13
match_list(a,k)