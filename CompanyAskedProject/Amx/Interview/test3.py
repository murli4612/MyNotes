def next_greater(nums):
    result = [-1] * len(nums)

    for i in range(len(nums)):
        for j in range( i +1, len(nums)):
            if nums[j] > nums[i]:
                result[i] = nums[j]
                break
            else:
                continue
    return result

nums = [4,5,2,10]
print(next_greater(nums))