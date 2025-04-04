class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


def linked_list_from_string(s):
    if not isinstance(s,str):
        return 'None'
    head = None
#     for i in range(len(s))[::-1][1:]:
#         new = Node(s[i])
#         new.next = head
#         head = new
#     return head
    elements = s.split(" -> ")
    elements = elements[:-1]
    for value in elements[::-1]:
        head = Node(int(value), head)

    return head
