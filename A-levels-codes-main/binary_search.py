# Binary search

def binary_search(arr, e):
    # Note that binary search are only for sorted arrays
    # ub = upper bound
    # lb = lower bound
    ub = len(arr)
    lb = 0
    found = False
    while not found:
        mid = round((ub + lb) / 2)
        if lb > len(arr):
            print("Not found")
            break
        if ub < 0:
            print("Not found")
            break
        if e == arr[mid]:
            print(f"Found at possition {mid + 1}")
            found = True
        elif e > arr[mid]:
            lb += 1
        else:
            ub -= 1

# Below code is just an illustarion for the code runner to see how the function works.
a_list = [2, 4, 8, 16, 32, 64, 128]
try:
    while True:
        opt = int(input("""
Choose an option:
1. Search for an element
2. exit
> """))
        if opt == 1:
            element = int(input("Enter the element you looking for: "))
            binary_search(a_list, element)
        elif opt == 2:
            break
except:
    print("Error")