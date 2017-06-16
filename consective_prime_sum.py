# https://projecteuler.net/problem=50
#
# Consecutive prime sum
# Problem 50
#
# The prime 41, can be written as the sum of six consecutive
# primes:

#     41 = 2 + 3 + 5 + 7 + 11 + 13
#
# This is the longest sum of consecutive primes that adds to
# a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand
# that adds to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum
# of the most consecutive primes?


def is_prime(num, primelist):
    filtered_result = filter(lambda x: num % x == 0, primelist)
    return len(filtered_result) == 0


def generate_moreprimes(primetotal, primelist):
    primelist_sum = sum(primelist)

    is_factor_of = lambda x: num % x == 0

    num = primelist[-1]
    while True:
        num += 1

        if not filter(is_factor_of, primelist):
            primelist.append(num)

            if (primelist_sum + num) >= primetotal:
                return (primelist, primelist_sum + num)


def is_consecutive_primesum(num, primelist):
    liststart = len(primelist) - 1
    pslice_sum = primelist[liststart]

    while pslice_sum < num and liststart > 0:
        liststart -= 1

        pslice_sum += primelist[liststart]
        if pslice_sum == num:
            return (True, primelist[liststart:len(primelist)])

    return (False, None)


def get_largest_specialprime(maxnum):
    primelist = [2]

    largest_specialprime = 1
    max_pslice_len = 1

    primelist_sum = sum(primelist)

    odd_nums = filter(lambda x: x % 2 != 0, range(2, maxnum + 1))

    for num in odd_nums:
        if not is_prime(num, primelist):
            continue

        if primelist_sum < num:
            primelist, primelist_sum = generate_moreprimes(num, primelist)

        ans, pslice = is_consecutive_primesum(num, primelist)

        if ans and len(pslice) > max_pslice_len:
            largest_specialprime = num
            max_pslice_len = len(pslice)

    # print('(CURRENT_ANS, pslice, pslice_len) = ({}, {}, {})'
    #                   .format(largest_specialprime, pslice, len(pslice)))

    return largest_specialprime


# -- main()
import time

# max_num = 1000
# max_num = 10000

# (ANS, timetaken): (16823, 0.565876960754)
# max_num = 20000

# (ANS, timetaken): (92951, 8.52132892609)
# max_num = 100000

# (ANS, timetaken): (499607, 12.8173229694)
# max_num = 500000

max_num = 1000000

start = time.time()
ans = get_largest_specialprime(max_num)
end = time.time()

timetaken = (end - start)

print('(ANS, timetaken): ({}, {})'.format(ans, timetaken))
