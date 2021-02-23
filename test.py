import math


def has_skip(pointer, jump, total_length):
    if (pointer % jump == 0 and pointer + jump < total_length):
        return True
    
    return False

def make_pointer(posting_list):
    jump = int(math.sqrt(len(posting_list)))
    result = []

    for i in range(len(posting_list)):
        if (has_skip(i, jump, len(posting_list))):
            result.append((posting_list[i], True, i + jump))
        else:
            result.append((posting_list[i], False, None))

    return result


print(make_pointer([1,5,8,9,10,13,15]))

def get_intersection(left, right):
    # left/right : [(1, True, 2), (5, False, None), (8, True, 4), (9, False, None),
    #               (10, True, 6), (13, False, None), (15, False, None)]

    left_pointer = 0
    right_pointer = 0

    result = []

    while (left_pointer < len(left) and right_pointer < len(right)):
        # print("===============")
        # print("LEFT_POINT:", left_pointer, "\nLEFT:", left)
        # print("RIGHT_POINT:", right_pointer, "\nRIGHT:", right)
        # print("===============")
        if (left[left_pointer][0] == right[right_pointer][0]):
            result.append(left[left_pointer][0])
            left_pointer += 1
            right_pointer += 1
        elif (left[left_pointer][0] < right[right_pointer][0]):
            if (left[left_pointer][1] and
                left[left[left_pointer][2]][0] <= right[right_pointer][0]):
                while (left[left_pointer][1] and
                       left[left[left_pointer][2]][0] <= right[right_pointer][0]):
                    left_pointer = left[left_pointer][2]
                continue

            left_pointer += 1
        else:
            if (right[right_pointer][1] and
                right[right[right_pointer][2]][0] <= left[left_pointer][0]):
                while (right[right_pointer][1] and
                       right[right[right_pointer][2]][0] <= left[left_pointer][0]):
                    right_pointer = right[right_pointer][2]
                continue

            right_pointer += 1

    return result


left = [(1, True, 2), (5, False, None), (8, True, 4), (9, False, None), (10, True, 6), (13, False, None), (15, False, None), (16, False, None)]
right = [(1, True, 2), (2, False, None), (3, True, 4), (4, False, None), (5, False, 6), (16, False, None)]

def test_intersection(left, right):
    left_pointer = make_pointer(left)
    right_pointer = make_pointer(right)
    
    return get_intersection(left_pointer, right_pointer) == sorted(list(set(left).intersection(set(right))))

print(test_intersection([1,2,3,4], [1,2,3,4]))
print(test_intersection([1,2,3,4], [5,6,7,8]))
print(test_intersection([5,6,7,8], [1,2,3,4]))

import random
from tqdm import tqdm

left = sorted(random.sample(range(1, 1000000), 500000))
right = sorted(random.sample(range(1, 1000000), 500000))

for i in tqdm(range(50,100)):
    random.seed(i)
    if (not test_intersection(left, right)):
        print(left)
        print(right)
        break

# import time

# start = time.perf_counter()
# test_intersection(left, right)
# end = time.perf_counter()
# print(end-start)