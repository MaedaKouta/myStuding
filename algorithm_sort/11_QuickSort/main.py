def partition(nums, beginning, ending):
    i = beginning - 1
    pivot = nums[ending]
    for j in range(beginning, ending):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[ending] = nums[ending], nums[i + 1]
    return i+1

def quick_sort(nums, beginning, ending):
    if beginning < ending:
        pivot_index = partition(nums, beginning, ending)
        quick_sort(nums, beginning, pivot_index - 1)
        quick_sort(nums, pivot_index + 1, ending)
    return nums


if __name__ == '__main__':
    nums = [55, 23, 19, 76, 3, 77, 19]
    print(quick_sort(nums, 0, len(nums) - 1))

