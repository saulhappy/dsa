from linked_list import LinkedList
from linked_list_reverse import reverse_linked_list


def compare_two_halves(first_half, second_half):
    while first_half and second_half:
        if first_half.data != second_half.data:
            return False
        else:
            first_half = first_half.next
            second_half = second_half.next
    return True

def palindrome(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    revert_data = reverse_linked_list(slow)
    check = compare_two_halves(head, revert_data)

    # revert_data = reverse_linked_list(revert_data) # why is this happening twice?

    if check:
        return True
    return False





    


# TEST CASES
# linked_list = LinkedList()

# linked_list.create_linked_list([1,2,3,4])
# result = palindrome(linked_list.head)
# print(result) # => False


linked_list = LinkedList()

linked_list.create_linked_list([1,2,3,2,1])
result = palindrome(linked_list.head)
print(result) # => True