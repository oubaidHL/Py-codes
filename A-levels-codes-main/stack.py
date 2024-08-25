# Stack

def push(item):
    global top, size, stack  # Remove global to edit edit the variables
    if top < size - 1:
        top += 1
        stack[top] = item
        print(f"{item} added to stack")
    else:
        print("Overflow, can't push.")


def pop():
    global top, base
    if top == base - 1:
        print("Underflow, can't pop.")
    else:
        print("pop done successfully!")
        stack[top] = None 
        top -= 1
        