class Solution(object):
    def middleNode(self, head):
        if not head.next:
            return head
        fast = head.next.next  
        isNotDiv = False
        while fast:
            if fast.next == None:
                head = head.next
                isNotDiv = True
                break
            head = head.next
            fast = fast.next.next
        return head if isNotDiv else head.next