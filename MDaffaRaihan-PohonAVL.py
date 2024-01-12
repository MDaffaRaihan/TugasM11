#Muhammad Daffa Raihan
#2IA25

class Node:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None


class AVLTree:
    def getHeight(self, node):
        if node is None:
            return 0
        return node.height

    def getBalance(self, node):
        if node is None:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def rotateRight(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))

        return x

    def rotateLeft(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  # Duplicate keys are not allowed

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        # Left Heavy
        if balance > 1:
            if key < root.left.key:
                return self.rotateRight(root)
            else:
                root.left = self.rotateLeft(root.left)
                return self.rotateRight(root)

        # Right Heavy
        if balance < -1:
            if key > root.right.key:
                return self.rotateLeft(root)
            else:
                root.right = self.rotateRight(root.right)
                return self.rotateLeft(root)

        return root

    def preOrder(self, root):
        if root:
            print(root.key, end=" ")
            self.preOrder(root.left)
            self.preOrder(root.right)


# Fungsi untuk meminta input dari pengguna dan membuat AVL Tree
def main():
    avl_tree = AVLTree()
    root = None

    n = int(input("Masukkan jumlah elemen yang akan dimasukkan: "))

    for _ in range(n):
        key = int(input("Masukkan nilai: "))
        root = avl_tree.insert(root, key)

    print("Preorder traversal dari AVL Tree:")
    avl_tree.preOrder(root)


if __name__ == "__main__":
    main()
