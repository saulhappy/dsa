from linked_list import LinkedList
from print_linked_list import print_list_with_forward_arrow


def remove_nth_last_node(head, n):
    left = head
    right = head

    for _ in range(n):
        right = right.next

    if right is None:
        return head

    while right.next is not None:
        right = right.next
        left = left.next
    
    left.next = left.next.next
    return head


# TEST CASES
linked_list = LinkedList()
linked_list.create_linked_list([23,28,10,5,67,39,70,28])
print("result before removal: ")
print_list_with_forward_arrow(linked_list.head)
print("\n")

result = remove_nth_last_node(linked_list.head, 4)
print("result after removal: ")
print_list_with_forward_arrow(linked_list.head)
