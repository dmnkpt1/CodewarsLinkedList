class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    stringified = ''
    if not isinstance(node,Node):
        return 'None'
    while node.next != None:
        stringified += f'{node.data}'
        stringified += ' -> '
        node = node.next
    stringified += f'{node.data} -> None'
    return stringified
