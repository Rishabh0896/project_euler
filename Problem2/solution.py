def sum_of_even_fibonacci_below_limit(upper_limit):
    """
    Calculate the sum of even Fibonacci numbers below a given limit.
    """
    # Initialize variables for Fibonacci sequence and sum of even numbers
    previous_number = 1
    current_number = 1
    even_sum = 0

    # Generate Fibonacci numbers until the current number exceeds the limit
    while current_number < upper_limit:
        # Check if the current Fibonacci number is even
        if current_number % 2 == 0:
            even_sum += current_number

        # Generate the next Fibonacci number
        next_number = previous_number + current_number

        # Update variables for the next iteration
        previous_number = current_number
        current_number = next_number

    return even_sum


if __name__ == "__main__":
    limit = 4000000
    print(sum_of_even_fibonacci_below_limit(limit))
