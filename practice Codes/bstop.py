'''
Author : Dhruv B Kakadiya

'''

class Node:
    def __init__(elf, data, pos):
        elf.key = data
        elf.pos = pos
        elf.right = None
        elf.left = None
def insert(root, key, pos):
    if root == None:root = Node(key, pos);print(pos)
    elif key < root.key:root.left = insert(root.left, key, pos=(2 * pos))
    else:root.right = insert(root.right, key, pos=(2 * pos + 1))
    return root
def minValueNode(node):
    current = node
    while (current.left is not None):current = current.left
    return current
def deleteNode(root, key, pr=True):
    if root is None:return
    elif key < root.key:root.left = deleteNode(root.left, key, pr)
    elif (key > root.key):root.right = deleteNode(root.right, key, pr)
    else:
        if pr:print(root.pos)
        if root.left is None and root.right is None:root = None
        elif root.left is None:root = root.right
        elif root.right is None:root = root.left
        else:temp = minValueNode(root.right);root.key = temp.key;root.right = deleteNode(root.right, temp.key, pr=False)
    return root
root = None
for _ in range(int(input())):
    op, x = input().split()
    if op == 'i':root = insert(root, int(x), 1)
    else:root = deleteNode(root, int(x))