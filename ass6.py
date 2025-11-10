size=10
table=[[] for _ in range(size)]

def hash_function(key):
    return key%size

def insert(key,value):
    index=hash_function(key)
    for pair in table[index]:
        if pair[0]==key:
            pair[1]=value
            print(f"updated key{key} with new value '{value}")
            return
    table[index].append([key,value])
    print(f"Inserted ('{key},{value}') at index{index}")

def search(key):
    index=hash_function(key)
    for pair in table[index]:
        if pair[0]==key:
            print(f"Found key={key}, value={pair[1]}")
            return
    print("key not found")

def delete(key):
    index=hash_function(key)
    for pair in table[index]:
        if pair[0]==key:
            table[index].remove(pair)
            print(f"deleted key:{key}")
            return
    print("key not found!")

def display():
    print("\n Hash table:")
    print(table)

while True:
    print("\n===Hash Table Program===")
    print("1)Insert key\n2)Search key \n3)Delete Key \n4)Display table \n5)Exit")
    choice=input("Enter your choice:")

    if choice == '1':
        key=int(input("Enter key(integer):"))
        value=input("Enter value:")
        insert(key,value)
    elif choice == '2':
        key=int(input("Enter key to search:"))
        search(key)
    elif choice == '3':
        key=int(input("Enter Key to delete:"))
        delete(key)
    elif choice == '4':
        display()
    elif choice == '5':
        print("Exiting program....Goodbye!")
        break
    else:
        print("Please enter valid choice[1-5]")
            

    
