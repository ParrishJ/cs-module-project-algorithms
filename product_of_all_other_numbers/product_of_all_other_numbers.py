'''
Input: a List of integers
Returns: a List of integers
'''
import math

def product_of_all_other_numbers(arr):

    # import math module
    # loop through array - at each index, set the value to 1, removing it from the final product. 
    # Use the math.prod to get product of rest of array, push that value to the products array,
    # then reset the index back to its initial value

    products = []
    
    temp = None

    for i in range(len(arr)):
        temp = arr[i]
        arr[i] = 1
        products.append(math.prod(arr))
        arr[i] = temp
        
    return products
    
#Made a slight imporovement on this by appending to empty array instead of copying entire array over 

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
