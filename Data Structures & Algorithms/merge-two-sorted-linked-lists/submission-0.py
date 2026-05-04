# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tailNode = dummy

        while list1 and list2:
            if list1.val < list2.val:
                chosenNode = list1
                list1 = list1.next
            else:
                chosenNode = list2
                list2 = list2.next
            tailNode.next = chosenNode
            tailNode = chosenNode
        
        tailNode.next = list1 or list2

        return dummy.next
