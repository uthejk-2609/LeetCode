# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy

        while curr.next:
            if curr.next.next and curr.next.val == curr.next.next.val:
                dup = curr.next.val
                while curr.next and curr.next.val == dup:
                    curr.next = curr.next.next
            else:
                curr = curr.next
        
        return dummy.next
