

def removeDuplicates(nums):
    index = duplicates_number = 0
    times = 1
    try:
        sample_element = nums[index]
        while True:
            next_index_to_check = index + times
            next_element = nums[next_index_to_check]
            if next_element == sample_element:
                times += 1
            else:
                del nums[index+1:next_index_to_check]
                sample_element = next_element
                index += 1
                times = 1

    except IndexError:
        pass

    return index + 1


assert removeDuplicates([1,2]) == 2
# assert removeDuplicates([]) == 0

l1 = [1,1,1,2,2,2,2,2,3]

length = removeDuplicates(l1)

assert l1 == [1,2,3]
assert length == 3