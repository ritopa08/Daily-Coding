10.

'''
 Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

'''

from itertools import combinations,permutations


s="abcba"
l=[]
    
for i in range(2,len(s)+1):
  x=list(combinations(s,i))
  l.extend(x)
#print(l)  

for i in range(len(l)):
  l[i]="".join(l[i])
#print(l)  


q=[]
for i in range(0,len(s)):
  p=[]
  x=""
  for j in range(i,len(s)):
    x = x + s[j]
    p.append(x)
  q.extend(p)  
#print(q)    

t=[]
for i in range(len(q)):
  v=q[i]
  f=set(v)
  h=len(f)
  s=len(v)
  if(h==2 and s>2):
    print(v)
          






