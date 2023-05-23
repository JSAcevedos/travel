class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = AVLNode(data)
        else:
            self.root = self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if node is None:
            return AVLNode(data)

        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        elif data > node.data:
            node.right = self._insert_recursive(node.right, data)
        else:
            # Duplicate values are not allowed in AVL tree
            return node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance_factor = self._get_balance_factor(node)

        if balance_factor > 1:
            if data < node.left.data:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
        elif balance_factor < -1:
            if data > node.right.data:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    def delete(self, data):
        self.root = self._delete_recursive(self.root, data)

    def _delete_recursive(self, node, data):
        if node is None:
            return node

        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            min_node = self._find_min_node(node.right)
            node.data = min_node.data
            node.right = self._delete_recursive(node.right, min_node.data)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance_factor = self._get_balance_factor(node)

        if balance_factor > 1:
            if self._get_balance_factor(node.left) >= 0:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
        elif balance_factor < -1:
            if self._get_balance_factor(node.right) <= 0:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    def _get_balance_factor(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _find_min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def print_tree(self):
        self._print_tree_recursive(self.root)

    def _print_tree_recursive(self, node):
        if node is None:
            return

        self._print_tree_recursive(node.left)
        print(node.data)
        self._print_tree_recursive(node.right)

    def find_shortest_path(self, place1, place2):
        root = self.find_parent_node(place1,place2)

        return self._distance(root,place1) + self._distance(root,place2) - 1

    def find_parent_node(self,data1,data2):
        parent = None
        temp = self.root
        if data1 > self.root.data and data2 > self.root.data:
            self.root = self.root.right
            parent = self.find_parent_node(data1,data2)
        elif data1 < self.root.data and data2 < self.root.data:
            self.root = self.root.left
            parent = self.find_parent_node(data1,data2)
        else:
            parent = self.root
        
        self.root = temp
        return parent
    
    def _distance(self,node,data):
        distance = 1
        while True:
            if node.data == data:
                break
            if node.data < data:
                node = node.right
                distance += 1
            else:
                node = node.left
                distance += 1

        return distance

places = ("Mongui", "Sachica", "Tinjaca", "Combita", "Chiquiza", "Sutamarchan", "Tibasosa", "Toca", "Guican", "Chivata", "Topaga", "Soraca", "Gameza", "Guayata", "Raquira", "Nobsa", "Tenza", "Aquitania")
tree = AVLTree()

for i in places:
    tree.insert(i)

towns = input().split()

print(tree.find_shortest_path(towns[0],towns[1]), end="")