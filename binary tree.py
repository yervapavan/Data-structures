class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
class Tree:
    def insert(self,root,data):
        if root is None:
            root=Node(data)
            return root
        q=[]
        q.append(root)
        while(len(q)>0):
            t=q[0]
            q.pop(0)
            if t.left is None:
                t.left=Node(data)
                break
            else:
                q.append(t.left)
            if t.right is None:
                t.right=Node(data)
                break
            else:
                q.append(t.right)
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)
l=list(map(int,input("enter elements to construct tree").split()))
root=None
t=Tree()
root=t.insert(root,l[0])
for i in range(1,len(l)):
    t.insert(root,l[i])
t.inorder(root)
                
