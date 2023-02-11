# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.value = x
       self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        node = A
        count = [0, 0]

        while node is not None:
            count[node.value] += 1
            node = node.next

        node = A

        for i in range(count[0]):
            node.val = 0
            node = node.next

        for i in range(count[1]):
            node.val = 1
            node = node.next

        print(A)
arr=[1,2,3,4,5,4,3,2,34,2,3]
obj=Solution()
for i in arr:
    obj.solve(i)
