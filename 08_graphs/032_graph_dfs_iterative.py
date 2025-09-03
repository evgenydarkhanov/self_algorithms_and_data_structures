# неориентированный граф задан списком смежности

from typing import (
    Any,
    Dict,
    List,
    Optional
)


def graph_traverse_dfs(
    graph: Dict[Any, List[Any]],
    start: Any
) -> Optional[List[Any]]:

    if not graph:
        return None

    visited = []
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])

    return visited


if __name__ == "__main__":
    graph = {
        'a': ['b', 'c'],
        'b': ['a', 'd', 'e'],
        'c': ['a', 'f'],
        'd': ['b'],
        'e': ['b', 'f'],
        'f': ['c', 'e'],
    }
                                                                 
    print(graph_traverse_dfs(graph, 'a'))
    print(graph_traverse_dfs(graph, 'e'))
