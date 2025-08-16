
def rotate_k_times(list,len, k):

    list[:k] = list[:k][::-1] 
    list[-(len-k):] = list[-(len-k):][::-1] 
    list[:] = list[::-1]
     




def rotate_k_times_brute(list, len, k):
    temp = []
    index = 0
    for i in range(k): 
        temp.append(list[i])


    for i in range(k,len):
        list[index] = list[i]
        index+=1
    
    for i in temp:
        print(i)
        list[index] = i
        index+=1

za_list = [1, 2, 3, 4, 5, 6, 7]
len = len(za_list)

rotate_k_times_brute(za_list, len, 3)

print(za_list)