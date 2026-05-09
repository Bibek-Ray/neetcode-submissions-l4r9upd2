# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        node = head
        rev = dummy
        cnt = 0

        while node:
            node = node.next
            cnt += 1

        to_remove = cnt - n + 1
        
        for i in range(to_remove):
            if i == to_remove - 1:
                del_val = dummy.next
                dummy.next = del_val.next
            else:
                dummy = dummy.next

        return rev.next