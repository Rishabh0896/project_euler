# Rationale behind solving the problem
# Natural numbers in consideration : [1, 1000)
# Multiples of 3 till LIMIT : [3, 999)
# So the sum of multiples of 3 would be 3(1 + 2 + 3 + 4 ... + 333) -- a
# Multiples of 5 till LIMIT : [3, 995) -- b
# So the sum of multiples of 3 would be 5(1 + 2 + 3 + 4 ... + 199) -- b
# Multiples of 15 till LIMIT : [3, 990) -- c
# So the sum of multiples of 3 would be 15(1 + 2 + 3 + 4 ... + 66) -- c
# We can do a + b - c as the multiples of 15 will be double counted
# To find the sums in a and b we can use gaussian sum formula no_of_terms(first_term + last_term)/2
def multiple_of_3_or_5_till_1000():
    """
    Calculates the sum of multiples of 3 or 5 below 1000.
    """
    limit = 1000
    sum_of_multiples_of_3 = sum_of_multiples_of_n_below_limit(3, limit)
    sum_of_multiples_of_5 = sum_of_multiples_of_n_below_limit(5, limit)
    sum_of_multiples_of_15 = sum_of_multiples_of_n_below_limit(15, limit)
    return sum_of_multiples_of_3 + sum_of_multiples_of_5 - sum_of_multiples_of_15


def sum_of_multiples_of_n_below_limit(n, limit):
    """
    Calculates the sum of multiples of 'n' below 'limit' using the Gaussian sum formula.
    """
    num_of_terms = (limit - 1) // n  # Counting the number of multiples below the limit
    return n * num_of_terms * (num_of_terms + 1) // 2


if __name__ == '__main__':
    print(multiple_of_3_or_5_till_1000())
