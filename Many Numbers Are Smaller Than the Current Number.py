def smallerNumbersThanCurrent(nums):
    result = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[j] < nums[i] and j != i:
                count += 1
        result.append(count)
    return result
nums = [8, 1, 2, 2, 3]
output = smallerNumbersThanCurrent(nums)
print(output)
