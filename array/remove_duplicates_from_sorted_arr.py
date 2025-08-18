list = [1,1,2,2,3,4,4]

def remove_dupli(list):
    i=0
    

    for j in range(1, len(list)):
        if list[i]!= list[j]:
            list[i+1] = list[j]
            i=i+1
    del list[i+1:]

remove_dupli(list)

print(list)

#bruteforce - append all the non zero into a different array, take a count for every zero on the first pass and
#then append all the zeroes at the end of the first loop