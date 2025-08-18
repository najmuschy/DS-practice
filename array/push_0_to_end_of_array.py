
def shift_zeroes(list):

    for i in range(len(list)):
        if list[i]==0:
            first_zero = i
            break
        
    for j in range(first_zero+1, len(list)):
        if list[j]!=0:
            list[first_zero], list[j] = list[j], list[first_zero]
            first_zero+=1


list = [1,0,0,3,4,5,0,7,8]

shift_zeroes(list)
print(list)