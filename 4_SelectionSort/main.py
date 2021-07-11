def selection_sort(nums):
    for i in range(len(nums)):
        min = i
        for j in range(i+1, len(nums)):
            if nums[min] > nums[j]:
                min = j
        nums[i], nums[min] = nums[min], nums[i]
    return nums


if __name__ == '__main__':
    nums = [5, 7, 9, 2, 10, 8]
    print(selection_sort(nums))