
def max_sub(list):
    maxx = 0

    for i in range(len(list)):
        sum=0
        for j in range(i, len(list)):
            sum=sum+list[j]
            maxx= max(maxx, sum)
    return maxx

list = [-2,-3,4,-1, -2, 1, -3]
print(max_sub(list))
