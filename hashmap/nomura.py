# Problem Description
#   In a trading system, you receive price quotes from multiple exchanges 
# for the same security. You need to calculate the Volume-Weighted Average Price 
# (VWAP) for each security across all exchanges.
#   VWAP = (Σ(Price × Volume)) / (Σ Volume)

#   Implement a function that processes a stream of quotes and returns the VWAP for each security.
#   Function Signature

from collections import defaultdict
# def calculate_vwap(quotes: List[Dict]) -> Dict[str, float]:
def calculate_vwap(quotes):

    """

    Args:

        quotes: List of dictionaries with keys: 'symbol', 'exchange', 'price', 'volume'

    Returns:

        Dictionary mapping symbol to VWAP

    """

    # include data quality check; the types will be correct
    # negative values - removed, or become 1

    # 0 values 
    # hashmap - key symbol-  list of (associated price, volume)

    # then, iterate through hashmap to calculate VWAP
    # default dict?



    prices_volume_map = defaultdict(list)

    for quote in quotes:
        symbol = quote["symbol"] 
        # if quote["symbol"]
        # (current num sum , current volume total)
        prices_volume_map[symbol].append((quote["price"], quote["volume"]))
    
    # mp = appl: (150, 1000) (200, 1000), googl: (2800, 300), (2801, 700)
    vwap = defaultdict(float)
    for symbol, values in prices_volume_map.item():
        vwap_numerator_sum = 0
        total_volume = 0
        for price, volume in values:
            vwap_numerator_sum += price * volume
            total_volume += volume

        vwap[symbol] = float(vwap_numerator_sum) / total_volume

    return vwap

#   Example Input
#   quotes = [

#       {'symbol': 'AAPL', 'exchange': 'NYSE', 'price': 150.00, 'volume': 1000},
#       {'symbol': 'AAPL', 'exchange': 'NYSE', 'price': 200.00, 'volume': 1000},

#       {'symbol': 'AAPL', 'exchange': 'NASDAQ', 'price': 150.50, 'volume': 2000},

#       {'symbol': 'AAPL', 'exchange': 'BATS', 'price': 149.75, 'volume': 500},

#       {'symbol': 'GOOGL', 'exchange': 'NYSE', 'price': 2800.00, 'volume': 300},

#       {'symbol': 'GOOGL', 'exchange': 'NASDAQ', 'price': 2801.00, 'volume': 700}

#   ]

#   Example Output

#   {
#       'AAPL': 150.214,  # (150*1000 + 150.5*2000 + 149.75*500) / 3500 = 150.214
#       'GOOGL': 2800.70  # (2800*300 + 2801*700) / 1000 = 2800.70
#   }