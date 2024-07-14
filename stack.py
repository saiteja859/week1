#Implementing Stack data structure
def is_empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)
    print(f"Item '{item}' pushed onto the stack.")

def pop(stack):
    if is_empty(stack):
        print("Stack is empty. No item to pop.")
        return None
    return stack.pop()

def peek(stack):
    if is_empty(stack):
        print("Stack is empty. No item to peek.")
        return None
    return stack[-1]

def display(stack):
    if is_empty(stack):
        print("Stack is empty.")
    else:
        print("Stack items are:", stack)

def display_menu():
    print("\nSelect an operation:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

if __name__ == "__main__":
    stack = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            item = input("Enter the item to push: ")
            push(stack, item)
        elif choice == '2':
            item = pop(stack)
            if item is not None:
                print(f"Item '{item}' popped from the stack.")
        elif choice == '3':
            item = peek(stack)
            if item is not None:
                print(f"Top item is '{item}'.")
        elif choice == '4':
            display(stack)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
