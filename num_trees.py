"""
SOURCE: https://leetcode.com/problems/unique-binary-search-trees/
"""

def num_trees(n):
    n_trees = [1] * (n + 1)

    for nodes in range(2, n + 1):
        total_trees = 0
        for root in range(1, nodes + 1):
            left = root - 1
            right = nodes - root
            total_trees += n_trees[left] * n_trees[right]
        n_trees[nodes] = total_trees
    
    return n_trees[n]

print(num_trees(n=0)) # => 1
print(num_trees(n=1)) # => 1
print(num_trees(n=2)) # => 2
print(num_trees(n=3)) # => 5
print(num_trees(n=4)) # => 14
print(num_trees(n=5)) # => 42
print(num_trees(n=6)) # => 132
print(num_trees(n=7)) # => 429
print(num_trees(n=8)) # => 1430
