class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None

    def insert(self,key):
        self.root=self._insert(self.root,key)

    def _insert(self,root,key):
        if root is None:
            return Node(key)
        if key<root.key:
            root.left=self._insert(root.left,key)
        elif key>root.key:
            root.right=self._insert(root.right,key)
        return root
    
    def search(self,key):
        return self._search(self.root,key)

    def _search(self,root,key):
        if root is None:
            return False
        if root.key==key:
            return True
        elif key<root.key:
            return self._search(root.left,key)
        else:
            return self._search(root.right,key)
    
    def delete(self,key):
        self.root=self._delete(self.root,key)

    def _delete(self,root,key):
        if root is None:
            return root
        if key<root.key:
            root.left=self._delete(root.left,key)
        elif key>root.key:
            root.right=self._delete(root.right,key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            min_larger_node=self._min_value_node(root.right)
            root.key=min_larger_node.key
            root.right=self._delete(root.right,min_larger_node.key)
        return root

    def min_value_node(self,node):
        current=node
        while current.left is not None:
            current=current.left
        return current
    
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.key , end=",")
            self.inorder(root.right)
    
bst=BST()

while True:
    print("====Binary search tree functions====")
    print("\n1.Insert \n2.Search \n3.Delete \n4.Display \n5.Exit")
    choice=input("Enter your choice[1-5]:")

    if choice=='1':
        key=int(input("Enter Value to Insert:"))
        bst.insert(key)
        print("Inserted!")
    elif choice=='2':
        key=int(input("Enter Value to Search:"))
        if bst.search(key):
            print("key found!")
        else:
            print("key not found")
    elif choice=='3':
        key=int(input("Enter Value to Delete:"))
        bst.delete(key)
        print("deleted if present.")
    elif choice=='4':
        print("BST inorder:", end=" ")
        bst.inorder(bst.root)
        print()
    elif choice=='5':
        print("Exiting program,Goodbye!")
    else:
        print("Please Enter valid choice[1-5].")

    
