class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Tree:
    def insert(self,root,data):
        if(root==None):
            root=Node(data)
            return root
        else:
            if(data<root.data):
                root.left=self.insert(root.left,data)
            elif(data>root.data):
                root.right=self.insert(root.right,data)
        return root
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
    def Vot(self,root,c,d):
        if root==None:
            return 
        try:
            d[c].append(root.data)
        except:
            d[c]=[root.data]
        self.Vot(root.left,c-1,d)
        self.Vot(root.right,c+1,d)
        
    def printvot(self,root):
        c=0
        d=dict()
        t1=Tree()
        t1.Vot(root,c,d)
        print(d)
        
l=list(map(int,input().split()))
t=Tree()
root=None
root=t.insert(root,l[0])
for i in range(1,len(l)):
    t.insert(root,l[i])
t.inorder(root)
t.printvot(root)
