from collections import deque
queue=deque()

def add_event(event):
    queue.append(event)
    print(f"Event added:{event}")

def process_event():
    if queue:
        eve=queue.popleft()
        print(f"Event processed:{eve}")
    else:
        print("No events to process.")

def display_events():
    if queue:
        print("\n Pending events:")
        for eve in queue:
            print(eve)
    else:
        print("No pending events.")

def cancel_event(event):
    if event in queue:
        queue.remove(event)
        print(f"\nEvent cancelled:{event}")
    else:
        print("Event not found in queue.")

while True:
    print("\n====Event Processing System====")
    print("\n1)Add Event \n2)Process Event \n3)Display Pending Events \n4)Cancel Event \n5)Exit\n")
    choice=input("Enter choice[1-5]:")

    if choice == '1':
        eve=input("Enter event to add:")
        if eve:
            add_event(eve)
        else:
            print("Event cannot be empty.")

    elif choice == '2':
        process_event()
    elif choice == '3':
        display_events()
    elif choice == '4':
        eve=input("Enter event to cancel:")
        if eve:
            cancel_event(eve)
        else:
            print("Please enter valid event name.")
    elif choice == '5':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Please enter valid choice[1-5]")