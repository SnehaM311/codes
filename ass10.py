class Node:
    def __init__(self, city, pop):
        self.city = city
        self.pop = pop
        self.left = None
        self.right = None

class CityBST:
    def __init__(self):
        self.root = None

    def insert(self, city, pop):
        city = city.strip()
        if self.root == None:
            self.root = Node(city, pop)
            print("City added.")
            return
        cur = self.root
        while True:
            if city == cur.city:
                cur.pop = pop
                print("Population updated.")
                return
            elif city < cur.city:
                if cur.left == None:
                    cur.left = Node(city, pop)
                    print("City added.")
                    return
                cur = cur.left
            else:
                if cur.right == None:
                    cur.right = Node(city, pop)
                    print("City added.")
                    return
                cur = cur.right

    def search(self, city):
        cur = self.root
        c = 0
        while cur:
            c += 1
            if city == cur.city:
                return cur, c
            elif city < cur.city:
                cur = cur.left
            else:
                cur = cur.right
        return None, c

    def delete(self, city):
        self.root = self._del(self.root, city)
        print("Delete operation done.")

    def _del(self, n, city):
        if n == None:
            return n
        if city < n.city:
            n.left = self._del(n.left, city)
        elif city > n.city:
            n.right = self._del(n.right, city)
        else:
            if n.left == None: return n.right
            if n.right == None: return n.left
            t = n.right
            while t.left:
                t = t.left
            n.city, n.pop = t.city, t.pop
            n.right = self._del(n.right, t.city)
        return n

    def update(self, city, pop):
        n, c = self.search(city)
        if n:
            n.pop = pop
            print("Population updated.")
        else:
            print("City not found.")

    def inorder(self, n):
        if n:
            self.inorder(n.left)
            print(n.city, ":", n.pop)
            self.inorder(n.right)

    def rev_inorder(self, n):
        if n:
            self.rev_inorder(n.right)
            print(n.city, ":", n.pop)
            self.rev_inorder(n.left)

    def max_depth(self, n):
        if n == None: return 0
        l = self.max_depth(n.left)
        r = self.max_depth(n.right)
        return 1 + (l if l > r else r)

    def count(self, n):
        if n == None: return 0
        return 1 + self.count(n.left) + self.count(n.right)


b = CityBST()
while True:
        print("\n1.Add\n 2.Delete \n3.Update \n4.Search \n5.desc \n6.asc \n7.Max Comparsions8 \n8.WorstCase \n9.Exit")
        ch = input("Choice: ")
        if ch == '1':
            c = input("City: ")
            p = int(input("Population: "))
            b.insert(c, p)
        elif ch == '2':
            c = input("City: ")
            b.delete(c)
        elif ch == '3':
            c = input("City: ")
            p = int(input("New Population: "))
            b.update(c, p)
        elif ch == '4':
            c = input("City: ")
            n, cnt = b.search(c)
            if n: print("Found", n.city, ":", n.pop, "(comparisons:", cnt, ")")
            else: print("Not found (comparisons:", cnt, ")")
        elif ch == '5':
            print("\nAscending order:")
            b.inorder(b.root)
        elif ch == '6':
            print("\nDescending order:")
            b.rev_inorder(b.root)
        elif ch == '7':
            print("Max comparisons:", b.max_depth(b.root))
        elif ch == '8':
            print("Worst case comparisons:", b.count(b.root))
        elif ch == '9':
            print("Goodbye!")
            break
        else:
            print("Enter valid choice.")


