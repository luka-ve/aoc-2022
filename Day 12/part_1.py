import numpy as np


test_result = 31


def main(input_file):
    # Read input
    with open(input_file, "r") as f:
        grid_alph = [[*line.strip()] for line in f]

    # Convert letters into numbers
    grid_num = []
    for row in grid_alph:
        grid_num.append([])
        for c in row:
            grid_num[-1].append(ord(c) - 96)

    # Convert to numpy array for easier access
    grid_num = np.array(grid_num)
    ascii_S = -13
    ascii_E = -27
    starting_pos = np.where(grid_num == ascii_S)
    end_pos = np.where(grid_num == ascii_E)
    grid_num[starting_pos] = 1
    grid_num[end_pos] = 27

    # Build directed graph
    graph: dict[str, list[str]] = dict()
    for y in range(grid_num.shape[0]):
        for x in range(grid_num.shape[1]):
            reachable_elevation = grid_num[y, x] + 1
            pos_string = f"{y},{x}"
            graph[pos_string] = []
            if (
                y < grid_num.shape[0] - 1
                and grid_num[y + 1, x] <= reachable_elevation + 1
            ):
                graph[pos_string].append(f"{y+1},{x}")
            if y >= 1 and grid_num[y - 1, x] <= reachable_elevation + 1:
                graph[pos_string].append(f"{y-1},{x}")
            if (
                x < grid_num.shape[1] - 1
                and grid_num[y, x + 1] <= reachable_elevation + 1
            ):
                graph[pos_string].append(f"{y},{x+1}")
            if x >= 1 and grid_num[y, x - 1] <= reachable_elevation + 1:
                graph[pos_string].append(f"{y},{x-1}")

    # Find shortest path
    shortest_path = bfs_shortest_path(
        graph,
        f"{starting_pos[0][0]},{starting_pos[1][0]}",
        f"{end_pos[0][0]},{end_pos[1][0]}",
    )

    return (
        len(
            bfs(
                graph,
                f"{starting_pos[0][0]},{starting_pos[1][0]}",
                f"{end_pos[0][0]},{end_pos[1][0]}",
            )
        )
        - 1
    )


def bfs_shortest_path(graph: dict[str, list[str]], node_start: str, node_end: str):

    path_list = [[node_start]]
    path_index = 0

    # Record previously recorded nodes to avoid cycles/backtracking
    previous_nodes = {node_start}

    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]

        # Target node found
        if node_end in next_nodes:
            current_path.append(node_end)
            return current_path

        # Add new paths
        for node in next_nodes:
            if not node in previous_nodes:
                new_path = current_path[:]
                new_path.append(node)
                path_list.append(new_path)

                previous_nodes.add(node)

        path_index += 1

    # No path found
    return []


def bfs(graph, node1, node2):
    visitedSet = set()
    queue = []
    visitedSet.add(node1)
    queue.append(node1)

    result = []
    while queue:
        v = queue[0]
        result.append(v)
        queue = queue[1:]
        print(queue)
        if node2 in graph[v]:
            return visitedSet

        for neighbor in graph[v]:
            if neighbor not in visitedSet:
                visitedSet.add(neighbor)
                queue.append(neighbor)
    return result
