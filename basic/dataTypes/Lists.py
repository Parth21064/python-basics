myList=['one','two','three','four']

# ordered sequence that can hold varity of objects
def printList(mylist):
    print(".............")
    for i in mylist:
        print(i)
    print(".............")

num_list=[2,8,3,5,1,6]

myList.append('five')

printList(myList)


print(num_list.pop())

printList(num_list)

# inplace sorting
num_list.sort()
printList(num_list)

# inplace reversed
myList.reverse()

printList(myList)

newList=[0,1,[2,3]]

printList(newList)

print(newList[2][1])

