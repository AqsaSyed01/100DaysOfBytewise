class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            print(f"Value {key} inserted.")
        else:
            self._insert(self.root, key)
            print(f"Value {key} inserted.")

    def _insert(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def delete(self, key):
        self.root, deleted = self._delete(self.root, key)
        if deleted:
            print(f"Value {key} deleted.")
        else:
            print(f"Value {key} not found.")

    def _delete(self, root, key):
        if root is None:
            return root, False

        deleted = False
        if key < root.val:
            root.left, deleted = self._delete(root.left, key)
        elif key > root.val:
            root.right, deleted = self._delete(root.right, key)
        else:
            deleted = True
            if root.left is None:
                return root.right, deleted
            elif root.right is None:
                return root.left, deleted

            min_larger_node = self._minValueNode(root.right)
            root.val = min_larger_node.val
            root.right, _ = self._delete(root.right, min_larger_node.val)

        return root, deleted

    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.val == key:
            return root

        if key < root.val:
            return self._search(root.left, key)
        
        return self._search(root.right, key)

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, root):
        res = []
        if root:
            res = self._inorder(root.left)
            res.append(root.val)
            res = res + self._inorder(root.right)
        return res

def main():
    bst = BinarySearchTree()
    while True:
        print("\nBinary Search Tree Operations:")
        print("1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. Display Inorder")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            key = int(input("Enter the value to insert: "))
            bst.insert(key)
        elif choice == 2:
            key = int(input("Enter the value to delete: "))
            bst.delete(key)
        elif choice == 3:
            key = int(input("Enter the value to search: "))
            result = bst.search(key)
            if result:
                print(f"Value {key} found in the BST.")
            else:
                print(f"Value {key} not found in the BST.")
        elif choice == 4:
            print("Inorder traversal of the BST: ", bst.inorder())
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
