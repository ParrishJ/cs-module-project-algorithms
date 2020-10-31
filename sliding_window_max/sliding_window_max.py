from collections import deque

'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
""" def sliding_window_max(nums, k):
    # Your code here

    #make an array to hold maxes
    max_list = []

    # make nested for loops to check for max
    for i in range(len(nums) - (k - 1)):
        k_list = []
        
        for j in range(k):
            k_list.append(nums[i + j])
        max_list.append(max(k_list))

    return max_list

arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

print(sliding_window_max(arr, k)) """

def sliding_window_max(nums, k):
    largest_list = []
    queue = deque()
    
    for i, j in enumerate(nums):
        while len(queue) > 0 and j > queue[-1]:
            queue.pop()

        queue.append(j)

        window = i - k + 1

        if window >= 0:
            largest_list.append(queue[0])

            if nums[window] == queue[0]:
                queue.popleft()

    return largest_list

#sliding window revised in sliding-window-2 file

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
