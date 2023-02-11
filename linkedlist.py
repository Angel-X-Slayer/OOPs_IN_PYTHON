class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head=None
    def Traversal(self):
        if self.head==None:
            print("the ll is empty !!!!!!")
        else:
            n=self.head
            while n!=None:
                print(n.data,end="-->>")
                n=n.ref
        print("\n")

    def Adding_first(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
        else:
            newnode.ref=self.head
            self.head=newnode
    
    def Adding_After(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
        else:
            n=self.head
            while n.ref!=None:
                n=n.ref
            n.ref=newnode

    def Adding_Any_After(self,data,spec):
        m=self.head
        while m!=None:
            if m.data==spec:
                break
            m=m.ref
        if m==None:
            print("the node is not present in the linkedlist")
            
        else:
            newnode=Node(data)
            newnode.ref=m.ref
            m.ref=newnode
    
    def Adding_Any_Before(self,data,spec):
        m=self.head
        while m!=None:
            if m.ref.data==spec:
                break
            m=m.ref
        if m!=None:
            print("there is no such node")
        else:
            newnode=Node(data)
            newnode.ref=m.ref
            m.ref=newnode

    def Delete_middle(self):
        fast=self.head
        slow=self.head
        if self.head !=None:
            while fast.ref!=None and slow.ref!=None:
                if fast.ref.ref!=None:
                    fast=fast.ref.ref
                    slow=slow.ref
                else:
                    fast=fast.ref
                    slow=slow.ref
            print("the middle element is:",slow.data)
            

        n=self.head
        while n.ref!=None:
            if n.ref.data==slow.data:
                p=n.ref.ref
                n.ref=p
            n=n.ref
    # def sorting(self):
    #     all=[]
    #     n=self.head
    #     if self.head==None:
    #         print("no element")
    #     elif n.ref==None:
    #         print(n.data)
    #     else:
    #         i=n
    #         j=n
    #         while 
            
        

    

LL1=LinkedList()
a=[00,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]
for i in a:
    LL1.Adding_After(i)
    
LL1.Traversal()
LL1.Delete_middle()
LL1.Traversal()
LL1.Adding_first(40)
LL1.Adding_After(10)
LL1.Adding_After(20)
LL1.Adding_After(80)
LL1.Adding_Any_After(60,40)
LL1.Adding_After(88)
LL1.Adding_first(101)
LL1.Adding_first(990)
LL1.Adding_After(11)
LL1.Adding_After(21)
LL1.Adding_After(81)
LL1.Adding_Any_After(60,80)
LL1.Adding_After(98)
LL1.Adding_first(201)
LL1.Adding_Any_Before(82,81)
LL1.Traversal()
LL1.Delete_middle()
LL1.Traversal()
