3.
'''
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left

'''

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
    def insert(self,data):
        #root=data
        if self.data:
            if data<=self.data:
                if self.left!= None:
                    self.left.insert(data)
                else:
                    self.left=Node(data)
            else:
                if self.right!= None:
                    self.right.insert(data)
                else:
                    self.right=Node(data)
                    
        else:
            self.data=data
            

#serializing
def serialized(root,l):
    if root!=None:
        l.append(root.data)    
        serialized(root.left,l)
        serialized(root.right,l)
    else:
        l.append("Nil") 


#De-serializing
def deserialized(d,l):
    if l[0]!="Nil":

        x=l.pop(0)
        d=Node(x)
        print(d.data)
        deserialized(d.left,l)
        deserialized(d.right,l)
    else:
        l.pop(0)




x=Node(0)
p= int(input())
for i in range(0,p):
    m=input()
    x.insert(m)

#serializing
l=[]
serialized(x,l)
print("serialized data:")
print(l) 

#deserializing
d=Node(None)
print("deserialized data:")
deserialized(d,l)
