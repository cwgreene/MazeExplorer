from collections import defaultdict

maze1 = """
+-+-+
|.|X|
+ + +
|. .|
+-+-+
"""

# States
SEPARATORLINE = "SEPARATORLINE"
NODELINE = "NODELINE"

def parse_maze_graph(maze):
    graph = {}
    state = "SEPARATORLINE"
    maze = [line for line in maze if line != ""]
    for lineno, line in enumerate(maze):
        for charpos, char in enumerate(line):
            if char == "\n":
                continue
            if state == SEPARATORLINE:
                above_node_pos = (lineno//2 - 1, charpos // 2)
                below_node_pos = (lineno//2, charpos // 2)
                graph[below_node_pos] = []
                if char not in "-+ ":
                    raise Exception("Invalid char '{}' at line {} pos {} on SEPARATORLINE"
                                .format(char, lineno, charpos))
                elif char == " ":
                    if lineno == 0:
                        raise Exception("Unclosed maze at line {} pos {}".format(lineno, charpos))
                    # add in below-node
                    graph[above_node_pos].append(below_node_pos)
                    graph[below_node_pos].append(above_node_pos)
                # don't care about walls
            if state == NODELINE:
                left_node = (lineno//2, charpos // 2)
                right_node = (lineno//2, charpos // 2 + 1)
                if char not in "|.X* ":
                    raise Exception("Invalid char '{}' at line {} pos {} on NODELINE".format(char, lineno, charpos))
                if char == " ":
                    if charpos % 2 != 0:
                        raise Exception("Invalid char '{}' at line {} pos {} on odd position"
                                .format(char, lineno, charpos))
                    graph[left_node].append(right_node)
                    graph[right_node].append(left_node)
                elif char == ".X*":
                    pass
        if state == SEPARATORLINE:
            state = NODELINE
        elif state == NODELINE:
            state = SEPARATORLINE
    result_graph = {}
    for node in graph:
        if graph[node]:
            result_graph[node] = graph[node]

    return result_graph

if __name__ == "__main__":
    print(parse_maze_graph(maze1.split("\n")))
