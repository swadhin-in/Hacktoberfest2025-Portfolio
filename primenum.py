import math

def is_prime(n):
    """
    Checks if a number n is prime using an optimized approach.
    """
    
    # 1. Handle base cases
    # Prime numbers must be greater than 1.
    if n <= 1:
        return False
        
    # 2 is the only even prime number.
    if n == 2:
        return True
        
    # All other even numbers are not prime.
    # This check also speeds up the loop by ruling out all even divisors.
    if n % 2 == 0:
        return False
        
    # 2. Check for odd divisors up to the square root
    # We only need to check for divisors up to the square root of n.
    # If n has a divisor larger than its square root, it must also
    # have a corresponding divisor smaller than its square root.
    limit = int(math.sqrt(n)) + 1
    
    # We start at 3 and check only odd numbers (step by 2).
    # We already ruled out 2 as a factor.
    for i in range(3, limit, 2):
        if n % i == 0:
            # We found a divisor, so n is not prime.
            return False
            
    # If the loop finishes without finding any divisors, n is prime.
    return True

# --- Examples from the prompt ---
print(f"Is 7 prime?   {is_prime(7)}")
print(f"Is 25 prime?  {is_prime(25)}")
print(f"Is 1 prime?   {is_prime(1)}")

# --- Example with a large prime number ---
# (1,000,000,007 is a known large prime)
print(f"Is 1000000007 prime? {is_prime(1000000007)}")
