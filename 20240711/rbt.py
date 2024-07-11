class Node:
    def __init__(self, data):
        self.data = data
        self.color = "RED"  # New nodes are always red
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(0)
        self.NIL.color = "BLACK"
        self.root = self.NIL

    def insert(self, key):
        new_node = Node(key)
        new_node.left = self.NIL
        new_node.right = self.NIL
        new_node.parent = None

        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.data < current.data:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        if new_node.parent is None:
            new_node.color = "BLACK"
            return

        if new_node.parent.parent is None:
            return

        self.fix_insert(new_node)

    def fix_insert(self, k):
        while k.parent.color == "RED":
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # uncle
                if u.color == "RED": # Case 1: Uncle is red
                    u.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.left: # Case 2: Node is a left child
                        k = k.parent
                        self.right_rotate(k)
                    # Case 3: Node is a right child
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right  # uncle
                if u.color == "RED": # Case 1: Uncle is red
                    u.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:# Case 2: Node is a right child
                        k = k.parent
                        self.left_rotate(k)
                    # Case 3: Node is a left child
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = "BLACK"

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def delete(self, key):
        node = self.search(self.root, key)
        if node == self.NIL:
            return

        self.delete_node(node)

    def delete_node(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self.rb_transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == "BLACK":
            self.fix_delete(x)

    def fix_delete(self, x):
        while x != self.root and x.color == "BLACK":
            if x == x.parent.left:
                w = x.parent.right
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self.left_rotate(x.parent)
                    w = x.parent.right

                if w.left.color == "BLACK" and w.right.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.right.color == "BLACK":
                        w.left.color = "BLACK"
                        w.color = "RED"
                        self.right_rotate(w)
                        w = x.parent.right

                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.right.color = "BLACK"
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self.right_rotate(x.parent)
                    w = x.parent.left

                if w.left.color == "BLACK" and w.right.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.left.color == "BLACK":
                        w.right.color = "BLACK"
                        w.color = "RED"
                        self.left_rotate(w)
                        w = x.parent.left

                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.left.color = "BLACK"
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = "BLACK"

    def rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def search(self, node, key):
        if node == self.NIL or key == node.data:
            return node

        if key < node.data:
            return self.search(node.left, key)

        return self.search(node.right, key)

    def minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node
    
    def inorder_traversal(self, node):
        if node != self.NIL:
            self.inorder_traversal(node.left)
            if node.data != 0:  # Ignoring the sentinel NIL node
                print(f"{node.data} ({node.color})", end=" ")
            self.inorder_traversal(node.right)
    def print_tree(self, node, indent="", last='updown'):
        if node != self.NIL:
            print(f"{indent}<{'R' if node.color == 'RED' else 'B'}-{node.data}>")
            indent += "   " if last == 'updown' else "|  "
            self.print_tree(node.left, indent, 'up')
            self.print_tree(node.right, indent, 'down')
# Driver code to test the implementation
if __name__ == "__main__":
    rbt = RedBlackTree()

    # Insert nodes
    rbt.insert(20)
    rbt.insert(15)
    rbt.insert(25)
    rbt.insert(10)
    rbt.insert(5)
    rbt.insert(1)

    # Test delete operation
    print("Before deletion:")
    rbt.inorder_traversal(rbt.root)
    
    print('Tree')
    rbt.print_tree(rbt.root)
    print() 

    rbt.delete(10)

    print("\nAfter deletion of 10:")
    rbt.inorder_traversal(rbt.root)
    
    print('Tree')
    rbt.print_tree(rbt.root)
    print() 
    
    rbt.delete(20)

    print("\nAfter deletion of 20:")
    rbt.inorder_traversal(rbt.root)
    
    print('Tree')
    rbt.print_tree(rbt.root)
    print() 
    