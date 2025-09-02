def recursion(num):
    if(num<=0):
        print(num)
        return
    # print(f'recursion call howar age {num}')
    recursion(num-3)

    print(num)

recursion(20)