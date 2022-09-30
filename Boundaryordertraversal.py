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
    def lot(self,root):
        if root is None:
           return
        q=[]
        q.append(root)
        while(len(q)>0):
            print(q[0].data,end=" ")
            node=q.pop(0)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
    def printLeaves(self,root):
        if(root):
            self.printLeaves(root.left)
            if root.left is None and root.right is None:
                print(root.data,end=" ")
            self.printLeaves(root.right)
    def printleftboundary(self,root):
        if root:
            if root.left:
                print(root.data,end=" ")
                self.printleftboundary(root.left)
    def printrightboundary(self,root):
        if root:
            if root.right:
                print(root.data,end=" ")
                self.printrightboundary(root.right)
                
    def bot(self,root):
        print(root.data,end=" ")
        t1=Tree()
        t1.printleftboundary(root.left)
        t1.printLeaves(root.left)
        t1.printLeaves(root.right)
        t1.printrightboundary(root.right)
        
l=list(map(int,input().split()))
t=Tree()
root=None
root=t.insert(root,l[0])
for i in range(1,len(l)):
    t.insert(root,l[i])
t.bot(root)
