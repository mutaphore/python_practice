#!/usr/local/bin/python

class BST(object):

    class Node(object):

        def __init__(self, val=None):
            self.left = None
            self.right = None
            self.data = val


    def __init__(self):
        self.root = None


    def insert_node(root, val):
        if root == None:
            root = BST.Node(val)
        else:
            if val < root.data:
                root.left = insert_node(root.left, val)
            else:
                root.right = insert_node(root.right, val)
        return root


    def insert(self, val):
        self.root = insert_node(self.root, val)


    def print_tree(self):
        if root == None:
            return
        else:
            print_tree(root.left)
            print root.data
            print_tree(root.right)


if __name__ == "__main__":
    bst = BST()

    bst.insert(10)
    bst.insert(5)
    bst.insert(2)
    bst.insert(4)
    bst.insert(8)
    bst.insert(1)
    bst.print_tree()
