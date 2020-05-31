
def find_path(position, target, graph):
    unexplored = set((position, None, None))
    while True:
        cur_node, parent, direction = unexplored.pop()
        explored[cur_node] = (parent, direction)
        for edge in graph[cur_node]["edges"]:
            direction, source, dest = edge
            if dest == target:
                return reconstruct_path(dest, explored)
            else:
                unexplored.add((dest, cur_node, direction))
        if len(unexplored) == 0:
            break
