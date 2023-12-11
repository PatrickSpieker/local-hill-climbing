import sys

def patrick_algo(array):
    candidate_index = int(len(array) / 2)
    steps = 0

    while True: 
        prev_value = array[candidate_index - 1] if candidate_index > 0 else -sys.maxsize
        next_value = array[candidate_index + 1] if candidate_index < len(array)-1 else -sys.maxsize
        candidate_value = array[candidate_index]

        if candidate_value > prev_value and candidate_value > next_value:
            # We found it
            return [candidate_index, steps]
        elif prev_value > candidate_value:
            steps += 1
            candidate_index -= 1
        else:
            steps += 1
            candidate_index += 1

def aaron_algo(nums):
    minVal, maxVal = 0, len(nums) - 1 # Valid search range is always [minVal, maxVal] (inclusive)
    elementsExamined = 0

    while minVal < maxVal:
        pivot = minVal + (maxVal - minVal) // 2 # Choose halfway point, rounding down
        elementsExamined += 1

        leftSideSmaller = pivot == 0 or nums[pivot - 1] < nums[pivot]
        rightSideSmaller = pivot == len(nums) - 1 or nums[pivot + 1] < nums[pivot]

        if leftSideSmaller and rightSideSmaller:
            return pivot, elementsExamined 
        elif rightSideSmaller:
            maxVal = pivot - 1 # Keep interval inclusive
        else: #leftSideSmaller or neither side smaller, in which case move in an arbitrary direction
            minVal = pivot + 1 # Keep interval inclusive

    return minVal, elementsExamined # There must always be a local maximum in this array, so if there is only one candidate, return it.