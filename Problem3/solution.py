def largest_prime_factor(n):
    """
    Function to find the largest prime factor of a given number.
    """
    largest_prime = 2
    i = 2
    while n > 1:
        if (n % i) == 0:
            largest_prime = i
            n //= i
        i += 1
    return largest_prime


if __name__ == "__main__":
    target_number = 600851475143
    print(largest_prime_factor(target_number))
