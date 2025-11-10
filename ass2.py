def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_indx=i
        for j in range(i+1,n):
            if arr[j]<arr[min_indx]:
                min_indx=j
        arr[i],arr[min_indx]=arr[min_indx],arr[i]
    return arr

def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

salaries=[45000,12000,25000,60000,40000,30000]

while True:
    print("\n====Employee Salary Sorting System===")
    print("\nSalaries:", salaries)
    print("\nMenu:")
    print("\n1)Selection sort \n2)Bubble Sort \n3)Top 5 salaries \n4)Exit")
    choice=input("Enter your choice[1-4]:")

    if choice=='1':
        sorted_salaries=selection_sort(salaries.copy())
        print("Salaries sorted using selection sort:")
        print(sorted_salaries)
    elif choice == '2':
        sorted_salaries=bubble_sort(salaries.copy())
        print("Salaries sorted using bubble sort:")
        print(sorted_salaries)
    elif choice == '3':
        top_5=sorted(salaries)[-5:][::-1]
        print("top 5 salaires are:")
        print(top_5)
    elif choice == '4':
        print("Exiting program")
        break
    else:
        print("Please enter valid choice[1-4].")