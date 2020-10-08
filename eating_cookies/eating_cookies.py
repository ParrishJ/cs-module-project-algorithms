'''
Input: an integer
Returns: an integer
'''
import sys

def eating_cookies(n):  
    possibilities = 0
    ways_to_eat = 3

    if n <= -1:
        return

    elif n == 0:
        possibilities = 1

    elif n == 1:
        possibilities = 1

    else: 
        def helper(n, currChoices):
            # base case - num_cookies == 0
            if n <= 0:
                nonlocal possibilities
                if n == 0:
                    possibilities += 1
                return

            for way in range(ways_to_eat):
            
                # make case if next possibility will make cookie monster eat too many cookies
                helper(n - (way + 1), currChoices + (way + 1))
        
        helper(n, 0)
        return possibilities
    return possibilities
        

    #return possibilities
       

print(eating_cookies(10))


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
