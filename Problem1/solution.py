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
