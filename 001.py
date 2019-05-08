## Multiples of 3 and 5
## If we list all the natural numbers below 10 that are multiples of 3 or 5,
## we get 3, 5, 6 and 9. The sum of these multiples is 23.
##
## Find the sum of all the multiples of 3 or 5 below 1000.

def main():
    total_sum = 0
    numbers_to_sum = 1000

    for i in range(numbers_to_sum):
        #print(i)
        if i%3 == 0 or i%5 == 0:
            print(i)
            total_sum += i
    print(total_sum)

main()
