# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        n = dummy
        set_nums = set(nums)

        while n.next is not None:
            if n.next.val in set_nums:
                n.next = n.next.next
                continue
            n = n.next
            

        return dummy.next
