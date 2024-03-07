class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow
