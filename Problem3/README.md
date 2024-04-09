# Problem Statement
The task is to find the largest prime factor of a given number.

# Approach
## Understanding the Problem
A prime factor of a number is a factor that is also a prime number. The largest prime factor is the largest prime number that divides the given number evenly.

## Rationale behind the Solution
The provided solution uses a simple approach to find the largest prime factor. It iterates through numbers starting from 2 up to the square root of the given number. For each number, it checks if it is a factor of the given number and if it is a prime number. If both conditions are met, it updates the largest prime factor accordingly. This approach ensures efficiency in finding the largest prime factor.

# Implementation Details
- The function `largest_prime_factor(n)` finds the largest prime factor of the given number `n`.
- It initializes `largest_prime` to 2 and iterates through numbers starting from 2.
- For each number, it checks if it is a factor of `n` and if it is a prime number.
- If both conditions are met, it updates `largest_prime` and divides `n` by the current number.
- Finally, it returns the largest prime factor found.

# Usage
To run the code, execute the `largest_prime_factor` function in the provided Python script. The result will be printed to the console.
```bash
python solution.py
```
