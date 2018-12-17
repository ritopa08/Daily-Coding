2. 
'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

'''


#defining function
def match_list(a,k):
  
  #initializes empty list
  l=[]
  
  #perform the multiplication opertions
  for i in range(k):
    
    #initializes x with 1
    x=1         
    for j in range(k):
      if i!=j:
        x=x*a[j]
        
        
    #add the result to the list    
    l.append(x)

  print(l)      

           


#Taking inputs    
a=[1, 2, 3, 4, 5]   #array of elements
n=len(a)            #size of the array

#calling the function
match_list(a,n)
