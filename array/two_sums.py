
def twoSum(nums: list[int], target: int) -> list[int]:
        tracker = dict()
        result = []
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in tracker:
                print(rem)
                result.extend([tracker[rem], i])
                
            tracker[nums[i]] = i
        print(tracker)
        return result

list = [2,7,11,15]


print(twoSum(list,9))