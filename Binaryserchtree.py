# # class Node:
# #     def __init__(self,data):
# #         self.data=data
# #         self.lchild=None
# #         self.rchild=None
# class BinaryST:
#     def __init__(self,data):
#         self.head=None
#         self.left=None
#         self.right=None
#     def insert(self,data):
#         if self.head==None:
#             self.head=data
#         elif self.head==data:
#             pass
#         else:
#             if self.head>data:
#                 if self.left==None:
#                     self.left=BinaryST(data)
#                 else:
#                     self.left.insert(data)
#             else:
#                 if self.right==None:
#                     self.right=BinaryST(data)
#                 else:
#                     self.right.insert(data)


#     # def __init__(self):
#     #     self.root=None
#     # def inserting(self,data):
#     #     Newnode=Node(data)
#     #     if self.root==None:
#     #         self.root=Newnode
#     #     else:
#     #         if self.root>data:
#     #             self.lchild.inserting(Newnode)
#     #         else:
#     #             self.root.rchild(Newnode)

# root=BinaryST(None)
# root.insert(10)

# class node:
#     def __init__(self,data):
#         self.key=data
#         self.left=None
#         self.right=None
# class BInaryst:
#     def __init__(self):
#         self.head=None
    
#     def insert(self,data):
#         if self.head==None:
#             newnode=node(data)
#             self.head=newnode
#         elif self.head.key==data:
#             pass
#         elif self.head.key>data:
#             if self.head.left==None:
#                 newnode=node(data)
#                 self.head.left=newnode
#             else:
#                 self.head.left.insert(data)
                
#         else:
#             if self.head.right==None:
#                 newnode=node(data)
#                 self.head.right=newnode
#             else:
#                 self.head.right.insert(data)
                
    
#     # def preorder(self):
#     #     print(self.head.key)
#     #     if self.head.left!=None:
#     #         # self.head.left.preorder()
#     #     else:
#     #         # self.right.preorder()



# root=BInaryst()
# # root.insert(10)
# # root.insert(5)
# l1=[11,23,22,55,45,34,76,67,99,87,90,111]
# for i in l1:
#     root.insert(i)
                


class BST:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

    def insert(self,data):
        if self.key==None:
            self.key=data
            return
        if self.key==data:
            return
        if self.key>data:
            if self.left==None:
                self.left=BST(data)
            else:
                self.left.insert(data)

        else:
            if self.right==None:
                self.right=BST(data)
            else:
                self.right.insert(data)
    def search(self,data):
        if self.key==data:
            print("node found")
            return
        if self.key>data:
            if self.left==None:
                print("node not found")
            else:
                self.left.search(data)
        else:
            if self.right==None:
                print("node not found")
            else:
                self.right.search(data)
    
    def preorder(self):
        print(self.key)
        if self.left!=None:
            self.left.preorder()
        
        if self.right!=None:
            self.right.preorder()
            
    def inorder(self):
        if self.left==None:
            pass
        else:
            self.left.inorder()
        print(self.key)
        if self.right==None:
            pass
        else:
            self.right.inorder()
            # return self
    def postorder(self):
        if self.left==None:
            pass
        else:
            self.left.postorder()
        if self.right==None:
            pass
        else:
            self.right.inorder()
        print(self.key)
        # return self

    def delete(self,data):
        if self.key==None:
            print("the tree is epty")
            return
        if data>self.key:
            if self.right!=None:
                self.right=self.right.delete(data) ##jokhon ekhane rr return er ki6u thaklo na tokhon previous function call ee nijr address ta return kore dilo, ei vabe recursiion ta kaj kor6 leora, bujhli ki bokachoda.....
            else:
                print("no such node")

        elif data<self.key:
            if self.left!=None:
                self.left=self.left.delete(data)##jokhon ekhane rr return er ki6u thaklo na tokhon previous function call ee nijr address ta return kore dilo, ei vabe recursiion ta kaj kor6 leora, bujhli ki bokachoda.....
            else:
                print("no such node")
        
        else:
            if self.left==None:
                temp=self.right
                self=None
                return temp
            elif self.right==None:
                temp=self.left
                self=None
                return temp
            else:
                node=self.right
                while self.left:
                    node=node.left
                self.key=node.key
                
                self.right=self.right.delete(node.key)
    # def count(self):
    #     if self.key==None:
    #         print (0)
    #     else:
    #         print (1+self.left.count()+self.right.count())



        
            

root=BST(None)
# l1=[11,9,23,22,55,45,34,76,67,99,87,90,111]
l1=[]
k=int(input("enter how many numbers you want to insert :"))
for i in range(k):
    num=int(input("enter the number :"))
    l1.append(num)
for i in l1:
    root.insert(i)

print("find 10:")
root.search(10)
print()
print("output in preorder fashion:")
root.preorder()
print()
print("output in inorder fashion:")
root.inorder()
print()
print("output in postorder fashion:")
root.postorder()
print()
print("deleting the node with key=11")
root.delete(90)
print()
print("after deleting,print in postorder fashion:")
root.postorder()

# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key
 
# # A utility function to insert
# # a new node with the given key
 
 
# def insert(root, key):
#     if root is None:
#         return Node(key)
#     else:
#         if root.val == key:
#             return root
#         elif root.val < key:
#             root.right = insert(root.right, key)
#         else:
#             root.left = insert(root.left, key)
#     return root
 
# # A utility function to do inorder tree traversal
 
 
# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.val)
#         inorder(root.right)
 
 
# # Driver program to test the above functions
# # Let us create the following BST
# #    50
# #  /     \
# # 30     70
# #  / \ / \
# # 20 40 60 80
 
# r = Node(50)
# r = insert(r, 30)
# r = insert(r, 20)
# r = insert(r, 40)
# r = insert(r, 70)
# r = insert(r, 60)
# r = insert(r, 80)
 
# # Print inoder traversal of the BST
# inorder(r)











