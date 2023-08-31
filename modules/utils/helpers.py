# modules/utils/helpers.py

def validate_ethereum_address(address):
    """
    Validate if the given string is a potentially valid Ethereum address.
    Note: This doesn't guarantee the address is active or has any balance, just that it's formatted correctly.
    """
    return address.startswith("0x") and len(address) == 42

def truncate_string(input_string, length=10):
    """
    Truncate the given string to the specified length and append '...' if it's longer.
    """
    if len(input_string) > length:
        return input_string[:length] + '...'
    return input_string

