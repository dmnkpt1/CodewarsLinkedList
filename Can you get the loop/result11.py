def loop_size(node):
    visited = {}
    index = 0

    while True:
        if node not in visited:
            visited[node] = index
            node = node.next
            index += 1
        else:
            start_index = visited[node]
            return index - start_index
