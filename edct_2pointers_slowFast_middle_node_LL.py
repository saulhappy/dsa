from linked_list import LinkedList

def get_middle_node(head):

    if head.next is None:
        return head

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# TEST CASES
linked_list = LinkedList()

# linked_list.create_linked_list([1, 2, 3, 4, 5])
# result = get_middle_node(linked_list.head)
# print(result.data) # => 3

linked_list.create_linked_list([1, 2, 3, 4, 5, 6])
result = get_middle_node(linked_list.head)
print(result.data) # => 4
