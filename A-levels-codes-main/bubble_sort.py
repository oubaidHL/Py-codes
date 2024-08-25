# Bubble sort

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:  # > sign for ascending, < for descending 
                arr[j], arr[j + 1] = arr[j+1], arr[j]  # Swapping
    return arr


# Below code is just an illustarion for the code runner to see how the function works.
user_list = []
while True:
    try:
        opt = int(input("""
Please select an option from below:
1. Sort elements 'bubble sort'
2. clear list
3. exit
> """))
        if opt == 1:
            lenth = int(input("Enter the size of the array: "))
            for i in range(lenth):
                user_list.append(int(input(f"Enter element {i + 1}: ")))
            print(f"List sorted successfully!")
            print(f"{bubble_sort(user_list)}")
        elif opt == 2:
            user_list.clear()
            print("Cleared successfully!")
        elif opt == 3:
            exit()
    except Exception as e:
        print(e)
