# Linked list - beginner concept

myLinkedList=[27,19,36,42,16,None,None,None,None,None]
myLinkedListPointer=[-1,0,1,2,3,6,7,8,9,10,11,-1]
startPointer=4
nullPointer=-1
def find(itemSearch):
    found=False
    itemPointer=startPointer
    print(itemPointer)
    while itemPointer!=nullPointer and not found:
        if myLinkedList[itemPointer]==itemSearch:
            found=True
        else:
            itemPointer=myLinkedListPointer[itemPointer]
            print("ItemPointer:",itemPointer)
            print("Pointer:",myLinkedListPointer[itemPointer])
    return itemPointer

 
# Below code is just an illustarion for the code runner to see how the function works.
item=int(input("Enter key to be searched:"))
result=find(item)
if result!=-1:
    print("Item found at",result)
else:
    print("Item not found")