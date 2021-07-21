
#BST is special typr of tree , where every node hase at most two child nodes and all the node to left are less than parent node and nodes to the  right side are greater than parent node

#BST does not have duplicate nodes

class BinarySearchTreeNode:
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self , data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def delete_node(self, val):
        if self.data < val:
            if self.left:
                self.left = self.left.delete_node(val)
        elif self.data > val:
            if self.right:
                self.right = self.right.delete_node(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            min_val = self.right.find_min() 
            self.data = min_val
            self.right = self.right.delete_node(min_val)
        return self.data

                
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in elements:
        root.add_child(i)

    return root

BST = build_tree([3,4,1,2,5,0,-1,-5,8,6,]) 
print(BST.in_order_traversal())
BST.delete_node(5)







