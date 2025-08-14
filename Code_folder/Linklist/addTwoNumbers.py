class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()
    tail = dummy
    carry = 0

    while l1 or l2 or carry:
        val = carry
        if l1:
            val += l1.val
            l1 = l1.next
        if l2:
            val += l2.val
            l2 = l2.next
        carry, out = divmod(val, 10)
        tail.next = ListNode(out)
        tail = tail.next

    return dummy.next

# Helper function to create a linked list from a list of digits
def create_linked_list(lst):
    dummy = ListNode()
    tail = dummy
    for val in lst:
        tail.next = ListNode(val)
        tail = tail.next
    return dummy.next

# Helper function to print a linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next

# Example usage:
# l1 represents 342 (2 -> 4 -> 3)
# l2 represents 465 (5 -> 6 -> 4)
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])

result = addTwoNumbers(l1, l2)
print("Result Linked List:")
print_linked_list(result)
