# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev_node = head
        if head:
            cur_node = head.next
        else:
            return head

        while cur_node:
            if prev_node.val == cur_node.val:
                prev_node.next = cur_node.next
                cur_node = cur_node.next
            else:
                prev_node = cur_node
                cur_node = cur_node.next
        
        return head