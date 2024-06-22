
def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize dummy, slow and fast pointers to reach middle of linked list...
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        # Find the middle of the linked list...
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # Delete the middle node...
        slow.next = slow.next.next
        return dummy.next
        