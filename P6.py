6.

'''
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. 
Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, 
since we pick 5 and 5..

'''

def sum_list(lst):
  l=[]
  x=lst
  for i in range(len(x)-2):
    s=x[i]
    m.append(s)
    for j in range(i+2,len(x)-1):
      if(x[j]>x[j+1]):
        s +=x[j]
      else:  
        s +=x[j+1] 
    l.append(s)  
  print(max(l))    
          
k=[2, 4, 6, 2, 5]
sum_list(k)