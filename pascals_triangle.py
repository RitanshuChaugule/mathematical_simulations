
list1 = [1,2,1]
list2 = []

k = 0

for i in range (0, 100):
    x = len(list1)
    y = x-1
    d = x+1
    list2.append(1)
    for j in range (0, y):
        k = (j+1)
        l = list1[j]+list1[k]
        list2.append(l)
    list1.extend(list2)
    for m in range (0, x):
        del list1[0]
        del list2[0]
    list1.append(1)
    print(list1)







