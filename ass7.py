TABLE_SIZE = 10

table = [None] * TABLE_SIZE
DELETED = object()   

def hash_index(key):
    return key % TABLE_SIZE

def insert(key):
    idx = hash_index(key)
    first_deleted = -1    
    for i in range(TABLE_SIZE):
        probe = (idx + i) % TABLE_SIZE
        slot = table[probe]

        if slot is None:
            target = first_deleted if first_deleted != -1 else probe
            table[target] = key
            print(f"Inserted key {key} at index {target}.")
            return

        if slot is DELETED:
            if first_deleted == -1:
                first_deleted = probe
            continue

        if slot == key:
            print(f"Key {key} already present at index {probe}.")
            return
        
    if first_deleted != -1:
        table[first_deleted] = key
        print(f"Inserted key {key} at index {first_deleted} (reused deleted slot).")
    else:
        print("Hash table is full. Insert failed.")

def search(key):
    
    idx = hash_index(key)
    for i in range(TABLE_SIZE):
        probe = (idx + i) % TABLE_SIZE
        slot = table[probe]
        if slot is None:
            break
        if slot is DELETED:
            continue
        if slot == key:
            print(f"Found key {key} at index {probe}.")
            return probe
    print(f"Key {key} not found.")
    return None

def delete(key):
    pos = search(key)
    if pos is None:
        print(f"Cannot delete {key}: not found.")
    else:
        table[pos] = DELETED
        print(f"Deleted key {key} from index {pos} (marked DELETED).")

def display():
    print("\nHash Table:")
    for i, slot in enumerate(table):
        if slot is None:
            val = "EMPTY"
        elif slot is DELETED:
            val = "DELETED"
        else:
            val = slot
        print(f"Index {i}: {val}")
    print()



while True:
        print("=== Linear Probing Hash Table ===")
        print("1. Insert key")
        print("2. Search key")
        print("3. Delete key")
        print("4. Display table")
        print("5. Exit")
        ch = input("Enter choice [1-5]: ").strip()

        if ch == '1':
            try:
                k = int(input("Enter key (integer): ").strip())
                insert(k)
            except ValueError:
                print("Please enter a valid integer.")
        elif ch == '2':
            try:
                k = int(input("Enter key to search: ").strip())
                search(k)
            except ValueError:
                print("Please enter a valid integer.")
        elif ch == '3':
            try:
                k = int(input("Enter key to delete: ").strip())
                delete(k)
            except ValueError:
                print("Please enter a valid integer.")
        elif ch == '4':
            display()
        elif ch == '5':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice — enter 1–5.")


