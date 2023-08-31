# modules/utils/conversions.py

def wei_to_eth(wei_value):
    """
    Convert Wei to Ether. 1 Ether = 10^18 Wei.
    """
    return wei_value / (10 ** 18)

def eth_to_wei(eth_value):
    """
    Convert Ether to Wei.
    """
    return eth_value * (10 ** 18)

