def linear_search(customer_ids,target_id):
    for i in customer_ids:
        if i== target_id:
            return True
    return False

def binary_search(customer_ids,target_id):
    low=0
    high=len(customer_ids)-1
    while low<=high:
        mid=(low+high)//2
        if customer_ids[mid]==target_id:
            return True
        elif customer_ids[mid]<target_id:
            low=mid+1
        else:
            high=mid-1
    return False

customer_ids=[1111,2222,3333,4444,5555,6666,7777]

while True:
    print("\n====E-commerce Customer id System====")
    print("\nCustomer ids:",customer_ids)
    print("\nMenu")
    print("\n1.Linear Search \n2.Binary Search \n3.Exit\n")
    choice=input("Enter Your choice[1-3]:")

    if choice == '1':
        target_id=int(input("Enter Customer id to search:"))
        if linear_search(customer_ids,target_id):
            print("Found the id using linear search!")
        else:
            print("Not Found using linear search!")
    elif choice == '2':
        target_id=int(input("Enter customer id to search:"))
        if binary_search(customer_ids,target_id):
            print("Found the id using binary search!")
        else:
            print("Not Found using binary search!")
    elif choice == '3':
        print("Exiting program, Goodbye!")
        break
    else:
        print("Please enter valid choice[1-3]")
        