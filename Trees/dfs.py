from treenode import TreeNode, sample_root_node, print_path, print_tree

print_tree(sample_root_node)

def dfs(root, target):
    if root.value == target:
        return root
    
    for child in root.children:
        node_found = dfs(child, target)
        
        if node_found != None:
            return node_found
   
    return None

search = dfs(sample_root_node, "F")
print(search)