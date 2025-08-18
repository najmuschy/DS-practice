#brutforce is done with the help of a visited array

def intersection(list1, list2):

    list = []
    i=0
    j=0

    while i!=len(list1) and j!=len(list2):

        if list1[i]==list2[j]:
            list.append(list1[i])
            i+=1
            j+=1
            
        else:
            i+=1

    return list

list1 =[1,2,3,4,5,5,7,7]
list2 =[1,2,3,4,5,5,7]

list = intersection(list1, list2)
print(list)