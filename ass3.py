undo_stack=[]
redo_stack=[]
document=""

def make_change(text):
    global document
    undo_stack.append(document)
    document+=text
    redo_stack.clear
    print("Change added successfully!")

def undo():
    global document
    if undo_stack:
        redo_stack.append(document)
        document=undo_stack.pop()
        print("Undo performed!")
    else:
        print("No actions to undo.")

def redo():
    global document
    if redo_stack:
        undo_stack.append(document)
        document=redo_stack.pop()
        print("Redo performed!")
    else:
        print("No actions to redo.")

def display_document():
    print("\n---Current Document---")
    if document:
        print(document)
    else:
        print("Document is empty.")
    print("-----------------------")


while True:
    print("\n====Simple Text Editor Program====")
    print("\nMenu:")
    print("\n1)Make a change \n2)Undo \n3)Redo \n4)Display DOcument \n5)Exit")
    choice=input("Enter your choice[1-5]:")

    if choice=='1':
        text=input("Enter text to add:")
        make_change(text)
    elif choice=='2':
        undo()
    elif choice=='3':
        redo()
    elif choice=='4':
        display_document()
    elif choice=='5':
        print("Exiting program. Good bye!")
        break
    else:
        print("Invalid Choice! Please enter valid chouce[1-5].")

    