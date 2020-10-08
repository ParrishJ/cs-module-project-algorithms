'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
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

print(sliding_window_max(arr, k))

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
