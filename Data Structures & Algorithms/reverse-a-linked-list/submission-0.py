# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # in a linked list there is a head reference that points to the first node 
        # and a tail reference that points to the last node 
        # so when reveresed the head and tail point to each others nodes
        #iterative approach is using 2 pointers: prev and curr 
        # next pointer that saves the node befroe we get rid of the chain
        #edge case: 
        if not head:
            return None

        prev = None 
        curr = head 
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next 
        return prev


        

        
        
        