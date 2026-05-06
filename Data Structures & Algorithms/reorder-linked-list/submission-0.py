# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = head
        node = head
        fir_node = head
        prev = None
        cnt = 0
        while dummy:
            dummy = dummy.next
            cnt += 1

        rng = int((cnt + (cnt % 2)) / 2)

        for i in range(rng):
            if i == rng - 1:
                sec_node = node.next
                node.next = None
            else:
                node = node.next
        
        while sec_node:
            nxt = sec_node.next
            sec_node.next = prev
            prev = sec_node
            sec_node = nxt
        
        while fir_node and prev:
            temp = fir_node.next
            fir_node.next = prev
            temp2 = prev.next
            prev.next = temp
            prev = temp2
            fir_node = temp

