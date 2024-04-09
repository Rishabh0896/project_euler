# Problem Statement

The problem requires finding the sum of all multiples of 3 or 5 below 1000.

# Approach

## Understanding the Problem

The problem involves finding the sum of all numbers that are multiples of either 3 or 5 but below 1000. To approach this efficiently, it's essential to understand the patterns of multiples of 3, multiples of 5, and their common multiples (multiples of 15).

## Rationale behind the Solution

- **Multiples of 3:** The multiples of 3 range from 3 to 999. We can find their sum using the Gaussian sum formula, considering the first term as 3, the last term as 999, and the number of terms as (999 // 3).
  
- **Multiples of 5:** The multiples of 5 range from 5 to 995. Again, we can apply the Gaussian sum formula considering the first term as 5, the last term as 995, and the number of terms as (995 // 5).

- **Multiples of 15:** Since multiples of 15 are common multiples of both 3 and 5, they get counted twice when calculating the sum. So, we need to subtract their sum from the total sum of multiples of 3 and 5.

## Implementation Details

- Implemented a function `sum_of_multiples_of_n_below_limit` to calculate the sum of multiples of a given number below a specified limit using the Gaussian sum formula.
  
- Calculated the sum of multiples of 3, multiples of 5, and multiples of 15 separately.
  
- Returned the sum of multiples of 3 and 5, subtracting the sum of multiples of 15 to avoid double-counting.

# Usage

To run the code, execute the `multiple_of_3_or_5_till_1000` function in the provided Python script. The result will be printed to the console.

```bash
python solution.py
```