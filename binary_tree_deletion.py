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
    def delete_deepest(self,root,d_node):
        q=[]
        q.append(root)
        while(len(q)>0):
            t=q.pop(0)
            if t is d_node:
                t=None
                return
            if t.left:
                if t.left is d_node:
                    t.left=None
                    return
                else:
                    q.append(t.left)
            if t.right:
                if t.right is d_node:
                    t.right=None
                    return
                else:
                    q.append(t.right)
         
    def delete(self,root,key):
        if root is None:
            return
        if root.left==None and root.right==None:
            if root.data==key:
                return None
            else:
                return root
        k_node=None
        q=[]
        q.append(root)
        while(len(q)>0):
            t=q[0]
            q.pop(0)
            if(t.data==key):
                k_node=t
            if(t.left):
                q.append(t.left)
            if(t.right):
                q.append(t.right)
        if k_node:
            k_node.data=t.data
            self.delete_deepest(root,t)
        return root
                
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
d=int(input("enter an element to delete"))
root=t.delete(root,d)
t.inorder(root)
                
