#bruteforce is through a set

def union(list1, list2):
    list =[]
    i=0
    j=0
    last= -2**63
    firstOver = False
    secondOver = False
    while True:

        if list1[i]<list2[j]:
            if list1[i]==last:
                i+=1
                continue
            last = list1[i]
            list.append(list1[i])
            i+=1
            if(i==len(list1)):
                firstOver= True
                break
        elif list1[i]>list2[j]:
            if list2[j]==last:
                j+=1
                continue            
            last = list2[j]
            list.append(list2[j])
            j+=1
            if(j==len(list2)):
                secondOver= True
                break
        
        elif list1[i] == list2[j]:
            if list1[i]==last:
                i+=1
                continue
            last = list1[i]
            list.append(list1[i])
            i+=1
            if(i==len(list1)):
                firstOver= True
                break        
    
    if(secondOver):
        while True:
            if list1[i]!= last:
                last=list1[i]
                list.append(list1[i])
                i+=1
            else:
                i=i+1
            if i==len(list1):
                break
    if(firstOver):
        while True:
            if list2[j]!=last:
                last=list2[j]
                list.append(list2[j])
                j=j+1
            else:
                j=j+1
            if j==len(list2):
                break
       
    return list

list1 =[1,3,4,5,6,8]
list2 =[1,2,3,4,9,11,11]

result = union(list1, list2)

print(result)
        