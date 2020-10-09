from collections import deque

arr = [1, 3, -1, -3, 5, 3, 6, 7]

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

print(sliding_window_max(arr, 2))


