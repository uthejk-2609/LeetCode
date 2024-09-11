# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head

        n = head
        while n.next:
            gcd_val = math.gcd(n.val, n.next.val)
            gcd_node = ListNode(gcd_val)
            gcd_node.next = n.next
            n.next = gcd_node
            n = gcd_node.next

        return head
