"""
Level Order Traversal - BFS

A Tree Algorithm where the nodes in a tree are visited in a level by level fashion.
i.e Nodes at each level are processed before moving on to the next.

Steps
    1. For every node, add to a queue.
    2. Process the node and pop from the front of the queue.
    3. Add its left and right child to the queue.

Time complexity  is O(N) since we visit every node at least once. N is the number of nodes in the tree.
Space complexity is O(N) since we make use of a queue data structure having a maximum of size N. 


Sample Binary Search Tree:

      8
     / \
    3   10
   / \    \
  1   6    14

Level-Order Traversal of this binary search tree results in:
output = [8,3,10,1,6,14]
"""

# Test Case
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
tree = Node(8)               
tree.left = Node(3)
tree.right = Node(10)
tree.left.left = Node(1)
tree.left.right = Node(6)
tree.right.right = Node(14)


# Code Implementation
def levelOrder(root):
    import collections
    start =  root
    queue  = collections.deque([]) # Initialize Queue
    queue.append(start) # Load the root node of tree into the queue
    output = []

    while queue:
        node = queue.popleft()       #  Get current node from queue.
        output.append(node.data)     #  Process the current node by appending to output.

        if node.left:                # Append its left child if any.
            queue.append(node.left)

        if node.right:               # Append its right child if any.
            queue.append(node.right)

    for val in output:               # Prints the node values in the output as space separated values.
        print(val, end=" ")

        
print(levelOrder(tree))


