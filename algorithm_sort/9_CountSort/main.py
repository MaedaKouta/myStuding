def count_sort(nums):
    max_num = max(nums)
    elements = [0] * (max_num + 1)
    ans = [0] * len(nums)

    for num in nums:
        elements[num] += 1

    for i in range(1, len(elements)):
        elements[i] += elements[i - 1]

    i = len(nums) - 1
    while i >= 0:
        index = nums[i]
        ans[elements[index] - 1] = nums[i]
        elements[index] -= 1
        i -= 1
    return ans

if __name__ == '__main__':
    nums = [23, 11, 36, 31, 8, 1]
    print(count_sort(nums))
