from collections import deque

def bfs(root_node, goal_value):
    path_queue = deque()
    initial_path = [root_node]
    path_queue.appendleft(initial_path)
    return None