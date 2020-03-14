#Find the max sum of subarray
A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def kadane(nums):
    a = b = nums[0]
    for x in nums[1:]:
        a = max(x, x+a)
        b = max(a, b)
    return b

def kadane2(nums):
    for x in range(1, len(nums)):
        if nums[x-1] > 0:
            nums[x] += nums[x-1]
    return max(nums)

print(kadane2(A))
