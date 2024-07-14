#Implementing Queue data structure
def is_empty(queue):
    return len(queue) == 0

def enqueue(queue, item):
    queue.append(item)
    print(f"{item} enqueued to the queue.")

def dequeue(queue):
    if is_empty(queue):
        print("Queue is empty. Cannot dequeue.")
        return None
    item = queue.pop(0)
    print(f"{item} dequeued from the queue.")
    return item
def size(queue):
    return len(queue)

def peek(queue):
    if is_empty(queue):
        print("Queue is empty.")
        return None
    return queue[0]

def display(queue):
    if not is_empty(queue):
        print("Queue contents:", queue)
    else:
        print("Queue is empty.")

def display_menu():
    print("\nQueue Operations Menu:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Size")
    print("6. Exit")
if __name__ == "__main__":
    queue = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")


        if choice == '1':
            item = input("Enter the item to enqueue: ")
            enqueue(queue, item)
        elif choice == '2':
            dequeue(queue)
        elif choice == '3':
            print("Front item:", peek(queue))
        elif choice == '4':
            display(queue)
        elif choice == '5':
            print("Queue size:", size(queue))
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
           print("Invalid choice. Please enter a number between 1 and 6.")
