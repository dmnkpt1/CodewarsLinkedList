from preloaded import Node

def swap_pairs(head):
    start_node = Node()
    start_node.next = head

    current_node = start_node

    while current_node.next and current_node.next.next:
        first_node = current_node.next
        second_node = first_node.next

        current_node.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node

        current_node = first_node

    return start_node.next
