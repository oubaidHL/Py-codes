# Linear search

def linear_search(arr, e):
    # Do not use arr.index() in linear_search
    found = False
    for i in range(len(arr)):
        if arr[i] == e:
            print(f"Found at possition {i + 1}")
            found = True
    if not found:
        print('Element not found')


# Below code is just an illustarion for the code runner to see how the function works.
a_list = [3, 1, 6, 98, 7]
while True:
    try:
        opt = int(input("""
Choose an option:
1. Search for an element
2. exit
> """))
        if opt == 1:
            element = int(input("Enter the element you looking for: "))
            linear_search(a_list, element)
        elif opt == 2:
            break
    except Exception as e:
        print(e)
