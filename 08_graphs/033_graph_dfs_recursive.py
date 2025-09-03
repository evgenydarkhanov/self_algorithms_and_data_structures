# неориентированный граф задан списком смежности

from typing import (
    Any,
    Dict,
    List,
    Optional
)


def graph_traverse_dfs(
    graph: Dict[Any, List[Any]],
    start: Any,
    visited: Optional[List] = None
) -> Optional[List[Any]]:

    if not graph:
        return None

    if visited is None:
        visited = []

    visited.append(start)

    for vertex in graph[start]:
        if vertex not in visited:
            graph_traverse_dfs(graph, vertex, visited)

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
