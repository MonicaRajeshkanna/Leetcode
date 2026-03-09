# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head):
        
        dummy = ListNode(0)
        curr = head
        
        while curr:
            prev = dummy
            
            # find position
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            
            next_temp = curr.next
            
            # insert
            curr.next = prev.next
            prev.next = curr
            
            curr = next_temp
        
        return dummy.next