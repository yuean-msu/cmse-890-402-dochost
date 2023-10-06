def have_digits(s: str) -> int:
    """Checks if a string has digits in it
    
    For example, for 'abc', return 0; for 'a2c', return 1.
    
    Args:
        s: the string to test.
    
    Returns:
        1 if the string has digits in it; 0 if not.
    
    """
    
    out = 0
    
    # loop through the string
    for c in s:
        # check if the character is a digit
        if c.isdigit():
            out = 1
            break
            
    return out