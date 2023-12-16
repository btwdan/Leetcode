
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        dummy = ListNode(-1)
        dummy.next = head
        
        current = dummy
        while current.next != None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
                
        return dummy.next