10.

'''
 Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

'''


#import packages 
from itertools import combinations,permutations

#input
s="abcba"
k=2

#initializes empty list
l=[]

#generate all the possible combinatons
for i in range(2,len(s)+1):
  x=list(combinations(s,i))
  
  #add to the list
  l.extend(x) 
 

 #converting list to string
for i in range(len(l)):
  l[i]="".join(l[i])
 


 
#generating all posible substring of the given string and stores in the list
q=[]
for i in range(0,len(s)):
  p=[]
  x=""
  for j in range(i,len(s)):
    x = x + s[j]
    p.append(x)
  q.extend(p)  
   

t=[]
for i in range(len(q)):
  v=q[i]      
  f=set(v)    #Remove duplicate entries
  h=len(f)    #length after removal of duplicates
  s=len(v)
  
  #checking conditions
  if(h==k and s>k):
    print(v)
          






