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
    def preorder(self,root):
        if root:
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):
        if root:
            self.postorder(root.right)
            self.postorder(root.left)
            print(root.data,end=" ")
l=list(map(int,input().split()))
t=Tree()
root=None
root=t.insert(root,l[0])
for i in range(1,len(l)):
    t.insert(root,l[i])
t.inorder(root)
t.preorder(root)
print()
t.postorder(root)
