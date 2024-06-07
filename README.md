# Prime Number Checker

This Python program checks whether a given number is a prime number or not.

## Description

A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. This program takes a number as input and determines if it is a prime number by checking if it has exactly two distinct divisors: 1 and the number itself.

## Usage

1. Open the terminal or command prompt.
2. Navigate to the directory where the `primeNumCheck1.py` file is located.
3. Run the program using the following command:

```
python primeNumCheck1.py
```

4. The program will output whether the given number (in this case, 23) is a prime number or not.

## Examples

- If the input number is 23, the output will be: `23 is a Prime Number`
- If the input number is 27, the output will be: `27 is not a Prime Number`

## Algorithm

The program uses the following algorithm to determine if a number is prime:

1. Check if the number is greater than 1 (since 1 is not considered a prime number).
2. Iterate through the range of numbers from 1 to the given number.
3. For each number in the range, check if the given number is divisible by that number using the modulus operator `%`.
4. Keep a count of the number of divisors.
5. If the count of divisors is exactly 2 (1 and the number itself), the number is prime.
6. Otherwise, the number is not prime.

## Contributing

Contributions to improve the program or the README file are welcome. Please submit a pull request or open an issue for any suggestions or bug reports.
