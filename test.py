list1 = [1,2,3]

list2 = list(list1)

def change():
    list2[0] = 10
    print(list1)

change()
print(list2)