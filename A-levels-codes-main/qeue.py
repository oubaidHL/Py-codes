# Qeue

def enqueue(value):
    global end, length, size, queue  # Remove global and edit the variables
    if end < size - 1:
        end += 1
        queue[end] = value
        length += 1

    else:
        print("Overflow, cannot enqeue")


def dequeue():
    global front, length, queue  # Remove global and edit the variables
    if length == 0:
        print("Underflow, cannot dequeue")
    else:
        queue[front] = None
        front += 1
        length -= 1

