# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head

        #Adding nodes to thr stack
        while curr:
            stack.append(curr)
            curr = curr.next

        curr = stack.pop()
        maxx = curr.val
        res = ListNode(maxx)

        while stack:
            curr = stack.pop()
            if curr.val < maxx:
                continue
            else:
                new_node = ListNode(curr.val)
                new_node.next = res
                res = new_node
                maxx = curr.val

        return res
