# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


# questions i'd ask
# what is the definition of a natural number? 

# assumptions i'd make
# no negatives
# exclusive of the int - eg. below 1000 doesn't include 1000

# input: integer, starting #
# output: integer, sum of multiples

# pseudocode
# define a function that takes in an integer
# define the blank return sum variable
# x = integer minus one
# while x is greater than 0:
    # if x / 3 or x / 5 is a whole number / isn't a decimal:
        # add the value of x to the sum
    # subtract one from x

# runtime - O(N) because it takes as long as the n of numbers integer-1 to zero?


def multiples_3_5(num):
    x = num - 1
    return_sum = 0

    while x > 0:
        if x % 3 == 0:
            return_sum += x

        if x % 5 == 0:
            return_sum += x

        x -= 1
    
    return return_sum


# test cases

# input: 10; output: 23
print(multiples_3_5(10))

# input: 100; output: ?
print(multiples_3_5(1000))