'''
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
 return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

'''



def mat(p,s):
  m=len(p)
  d=len(s)
  t=[]
  q=""
  for i in range (d):
    x=s[i]
    for k in range(m):
      if(p[k]==x[k]) : 
        q +=x[k] 
      else:
        q= " " 
    if(len(q)>=m):
      t.append(x)
        
  print(t)      

    


s=['road','roar','root','roap']
p='roa'  
if(type(p)==list):
  #converting list to string
  p=" ".join(map(str,p))   
mat(p,s)
