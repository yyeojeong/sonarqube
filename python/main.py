def calculate_factorial(n):
    """
    Calculate the factorial of a given non-negative integer.
    
    Args:
    n (int): A non-negative integer
    
    Returns:
    int: The factorial of n
    
    Raises:
    ValueError: If n is negative
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)