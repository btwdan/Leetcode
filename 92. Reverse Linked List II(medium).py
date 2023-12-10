class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        curr = ListNode(0)
        curr_2 = curr
        curr_2.next = head

        tmp = head

        for i in range(1, left):
            curr_2 = tmp
            tmp = tmp.next

        first = tmp
        for i in range(left,right):
            curr_head = curr_2.next
            next_head = first.next

            curr_2.next = next_head
            first.next = next_head.next
            next_head.next = curr_head

        return curr.next