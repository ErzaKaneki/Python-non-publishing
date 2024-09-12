from treenode import TreeNode, sample_root_node, print_path, print_tree

print_tree(sample_root_node)

def dfs(root, target):
    if root.value == target:
        return root
    return None