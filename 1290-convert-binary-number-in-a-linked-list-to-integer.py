class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        current = head
        temp = head
        total = 0
        idx = self.get_length(temp)
        while current:
            total += current.val * (2 ** (idx - 1))
            idx -= 1 
            current = current.next
        return total
    
    def get_length(self, list_node: ListNode):
        length = 0
        while list_node:
            length += 1
            list_node = list_node.next
        return length