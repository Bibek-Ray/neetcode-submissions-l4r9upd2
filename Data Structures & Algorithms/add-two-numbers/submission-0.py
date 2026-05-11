# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""
        dummy = ListNode(0)
        prev = None

        while l1:
            num1 = str(l1.val) + num1
            l1 = l1.next

        while l2:
            num2 = str(l2.val) + num2
            l2 = l2.next

        num3 = int(num1) + int(num2)

        num3_st = str(num3)

        for ch in num3_st:
            dummy = ListNode(int(ch), next=prev)
            prev = dummy
        
        return dummy



