def time_to_buy(nums):
    
    mini, profit = nums[0], 0

    for i in range(1, len(nums)):   
        cost = nums[i]-mini
        profit = max(profit, cost)
        mini = min(nums[i], mini)
    
    return profit

list = [7,1,5,3,6,4]
    
print(time_to_buy(list))