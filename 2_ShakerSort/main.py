def shaker_sort(nums):
    beginning = 0
    ending = len(nums) - 1

    while beginning < ending:
        for i in range(beginning, ending):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        ending -= 1

        for i in range(ending - 1, beginning - 1, -1):
            print(i)
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        beginning += 1

    return nums


if __name__ == '__main__':
    nums = [65, 45, 66, 4, 89, 50, 24, 43, 99, 14]
    print(shaker_sort(nums))
