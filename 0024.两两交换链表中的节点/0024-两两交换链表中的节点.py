# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        p1 = head

        if not p1:
            return None

        if not p1.next:
            return head
        else:
            new_head = p1.next
            p2 = p1.next

        pre_node = None
        while p1 and p2:
            #print(p1.val,p2.val)
            p1.next = p2.next
            p2.next = p1
            if pre_node:
                pre_node.next = p2
            pre_node = p1

            if p1.next and p1.next.next:
                p1 = p1.next
                p2 = p1.next
            else:
                break

        return new_head
