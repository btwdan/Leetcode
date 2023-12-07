# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        resList = ListNode(0)
        dummy = resList
        count = 0
        k = 0

        while l1 and l2:
            if (k == 1):

                if ((l1.val + l2.val + 1) > 9):
                    count = (l1.val + l2.val + 1) - 10
                    dummy.next = ListNode(count)
                    k = 1
                else:
                    count = l1.val + l2.val + 1
                    dummy.next = ListNode(count)
                    k = 0

            else:

                if ((l1.val + l2.val) > 9):
                    count = (l1.val + l2.val) - 10
                    dummy.next = ListNode(count)
                    k = 1
                else:
                    count = l1.val + l2.val
                    dummy.next = ListNode(count)

            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            if(l1.val == 9 and k == 1):
                dummy.next = ListNode(0)

            elif(l1.val < 9 and k == 1):
                dummy.next = ListNode(l1.val + 1)
                k = 0
            else:
                dummy.next = ListNode(l1.val)
            
            dummy = dummy.next
            l1 = l1.next
        
        while l2:
            if(l2.val == 9 and k == 1):
                dummy.next = ListNode(0)

            elif(l2.val < 9 and k == 1):
                dummy.next = ListNode(l2.val + 1)
                k = 0
            else:
                dummy.next = ListNode(l2.val)

            dummy = dummy.next
            l2 = l2.next
            
            
        if (k == 1):
            dummy.next = ListNode(1)

        return resList.next