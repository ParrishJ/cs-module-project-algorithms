'''
Input: an integer
Returns: an integer
'''
import sys

""" def eating_cookies(n):  
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
    return possibilities """
        

def eating_cookies2(n, cache={}):

    if n <= -1:
        return 0

    elif n == 0:
        return 1

    elif n == 1:
        return 1
       
    elif n in cache:
        return cache[n]
    else:
        cache[n] = eating_cookies2(n-3, cache) + eating_cookies2(n-2, cache) + eating_cookies2(n-1, cache)
        return eating_cookies2(n-3, cache) + eating_cookies2(n-2, cache) + eating_cookies2(n-1, cache)

print(eating_cookies2(100))

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies2(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
