# Basic mathematical operations used by main.py


def power(base, exp):
    """Return base raised to exp."""
    return base ** exp


def factorial(n):
    """Return n! recursively; raises ValueError for negative n."""
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    if n == 0:
        return 1  # base case
    return n * factorial(n - 1)


def gcd(a, b):
    """Return the greatest common divisor using Euclid's algorithm."""
    if b == 0:
        return a  # base case: b reached zero
    return gcd(b, a % b)


def is_prime(n):
    """Return True if n is a prime number (trial division up to sqrt(n))."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  # found a factor
    return True


if __name__ == "__main__":
    assert power(2, 10) == 1024
    assert factorial(5) == 120
    assert gcd(48, 18) == 6
    assert is_prime(97) is True and is_prime(4) is False
    print("sci_calc self-tests passed")
