class Node:
    def __init__(self,roll,name,marks):
        self.roll=roll
        self.name=name
        self.marks=marks
        self.next=None

class StudentList:
    def __init__(self):
        self.head=None
    
    def add(self,roll,name,marks):
        new=Node(roll,name,marks)
        if self.head==None:
            self.head=new
        else:
            t=self.head
            while t.next!=None:
                t=t.next
            t.next=new
        print("Student added successfully!")
    
    def display(self):
        if self.head==None:
            print("No records found!")
        else:
            t=self.head
            print("\nRoll\tName\tMarrks")
            print("----------------------------------")
            while t!=None:
                print(f"\n{t.roll}\t{t.name}\t{t.marks}")
                t=t.next

    def search(self,roll):
        t=self.head
        while t!=None:
            if t.roll==roll:
                print(f"Found-> Roll:{t.roll} , Name:{t.name} , Marks:{t.marks}")
                return
            t=t.next
            print("Student not found!")
    
    def delete(self,roll):
        t=self.head
        prev=None
        while t!=None:
            if t.roll==roll:
                if prev==None:
                    self.head=t.next
                else:
                    prev.next==t.next
                return
            prev=t
            t=t.next
        print("Student not found.")

    def sort(self,key):
        if self.head==None:
            print("No records to sort.")
        else:
            arr=[]
            t=self.head
            while t!=None:
                arr.append((t.roll,t.name,t.marks))
                t=t.next
            if key=="roll":
                arr.sort(key=lambda x:x[0])
            elif key=="marks":
                arr.sort(key=lambda x:x[2])

            t=self.head
            for r,n,m in arr:
                t.roll=r
                t.name=n
                t.marks=m
                t=t.next

s=StudentList()

while True:
    print("====Student Record Management====")
    print("1)Add Student \n2)Display Students \n3)Search Students \n4)Delete Student \n5)Sort by Roll no. \n6)Sort by marks \n7)Exit")
    choice=input("Enter Your choice[1-7]:")

    if choice=='1':
        roll=int(input("Enter Roll no:"))
        name=(input("Enter Name:"))
        marks=float(input("Enter Marks:"))
        s.add(roll,name,marks)
    elif choice=='2':
        s.display()
    elif choice=='3':
        roll=int(input("Enter Roll no to search:"))
        s.search(roll)
    elif choice=='4':
        roll=int(input("Enter Roll no to delete:"))
        s.delete(roll)
    elif choice=='5':
        s.sort("roll")
    elif choice=='6':
        s.sort("marks")
    elif choice=='7':
        print("Exiting Pregram.Goodbye!")
    else:
        print("Please enter valid choice[1-7].")


