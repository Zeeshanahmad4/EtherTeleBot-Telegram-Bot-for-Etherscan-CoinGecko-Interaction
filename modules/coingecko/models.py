# modules/coingecko/models.py

class CryptoCurrency:
    def __init__(self, id, symbol, name, current_price, market_cap, market_cap_rank, 
                 total_volume, price_change_percentage_24h, market_dominance, circulating_supply):
        self.id = id  # The unique ID of the cryptocurrency on CoinGecko.
        self.symbol = symbol.upper()  # The symbol of the cryptocurrency (e.g., "BTC" for Bitcoin).
        self.name = name  # The name of the cryptocurrency (e.g., "Bitcoin").
        self.current_price = current_price  # Current price in USD.
        self.market_cap = market_cap  # Market capitalization in USD.
        self.market_cap_rank = market_cap_rank  # Rank based on market cap.
        self.total_volume = total_volume  # Total volume in last 24 hours.
        self.price_change_percentage_24h = price_change_percentage_24h  # Price change percentage in the last 24 hours.
        self.market_dominance = market_dominance  # Percentage of market dominance.
        self.circulating_supply = circulating_supply  # Current circulating supply.

    def __repr__(self):
        return f"<CryptoCurrency(name={self.name}, symbol={self.symbol}, current_price=${self.current_price:.2f})>"

