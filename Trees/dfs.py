from treenode import TreeNode, sample_root_node, print_path, print_tree

print_tree(sample_root_node)

def dfs(root, target, path = ()):
    path += (root,)
    if root.value == target:
        return path
    
    for child in root.children:
        path_found = dfs(child, target, path)
        
        if path_found != None:
            return path_found
   
    return None

search = dfs(sample_root_node, "F")
print(search)