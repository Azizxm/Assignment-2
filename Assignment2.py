"""
Name : Aziz mohmand
Date: 06/16/2024
Description: This program determines prime numbers up to a user-specified upper bound
             using the Sieve of Eratosthenes algorithm.
"""

def sieve_of_eratosthenes(upper_bound):
    """
    Function to calculate prime numbers up to a given upper bound using the Sieve of Eratosthenes algorithm.
    
    Parameters:
    upper_bound (int): The upper limit up to which we want to find prime numbers.
    
    Returns:
    list: A list of prime numbers up to the specified upper bound.
    """
    # Create a list of boolean values, with True indicating that the index is a prime number
    is_prime = [True] * (upper_bound + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
    
    p = 2
    while p * p <= upper_bound:
        if is_prime[p]:
            for multiple in range(p * p, upper_bound + 1, p):
                is_prime[multiple] = False
        p += 1
    
    # Extracting prime numbers from the boolean list
    primes = [num for num in range(upper_bound + 1) if is_prime[num]]
    
    return primes

def get_upper_bound():
    """
    Function to prompt the user for an upper bound and validate the input.
    
    Returns:
    int: A valid upper bound specified by the user.
    """
    while True:
        try:
            upper_bound = int(input("Enter an upper bound between 2 and 1000: "))
            if 2 <= upper_bound <= 1000:
                return upper_bound
            else:
                print("Please enter an integer between 2 and 1000.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    """
    Main function to run the prime number analysis and display the results.
    """
    upper_bound = get_upper_bound()
    primes = sieve_of_eratosthenes(upper_bound)
    
    print(f"Prime numbers up to {upper_bound}:")
    for prime in primes:
        print(prime, end=' ')
    print()

if __name__ == "__main__":
    main()
