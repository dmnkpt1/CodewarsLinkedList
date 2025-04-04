from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
 
def get_nth(node, index):
    nodes = []
    while node is not None:
        nodes.append(node)
        node = node.next
    if  index < 0 or len(nodes) <= index:
        raise IndexError
    return nodes[index]

