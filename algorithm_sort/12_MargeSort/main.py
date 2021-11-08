def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    split = len(nums) // 2
    left = nums[:split]
    right = nums[split:]

    left = merge_sort(left)
    right = merge_sort(right)

    i, j, k= 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1

    return nums


if __name__ == '__main__':
    nums = [32, 4, 55, 99, 34, 21, 18]
    print(merge_sort(nums))