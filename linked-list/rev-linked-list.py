# Problem 206
# Run   O(n)
# Space O(1)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = head
        prevNode = None
        nextNode = None

        while root:
            nextNode = root.next
            root.next = prevNode

            prevNode = root
            root = nextNode
        
        return prevNode
