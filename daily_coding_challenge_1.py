1. 
'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

'''

#defining a function
def match_list(a,k):
  #Initializes empty list
  l=[]       
  
  
  #calculate the sum of two numbers in the list
  for i in range(len(a)):
    for j in range(i+1,len(a)):
      s=a[i]+a[j]
      
      #add each sum to the list
      l.append(s)    
      
      
  #Remove duplicates from the list    
  l=set(l)
  
  #checking whether element is present in the list
  if k in (l):
    print("true")
  else:
    print("false")        

    
    
#taking inputs
a=[10, 15, 3, 7]   #array containing numbers
k=13               #element to be searched

#calling function
match_list(a,k)    
