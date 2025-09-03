# неориентированный граф задан списком смежности

from collections import deque
from typing import (
    Any,
    Dict,
    List,
    Optional
)


def graph_traverse_bfs(
    graph: Dict[Any, List[Any]],
    start: Any
) -> Optional[List[Any]]:

    if not graph:
        return None

    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])

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
                                                                 
    print(graph_traverse_bfs(graph, 'a'))
    print(graph_traverse_bfs(graph, 'e'))
