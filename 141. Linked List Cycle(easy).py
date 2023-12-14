class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        self.vizit = False

class Solution(object):
    def hasCycle(self, head):
        if head == None or head.next == None:
            return False
        if head.next.next:
            head_next = head.next.next
        else:
            return False
        while head and head_next and head_next.next:
            if head == head_next:
                return True
            head = head.next
            head_next = head_next.next.next

        return False