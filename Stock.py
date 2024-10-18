# Predefined stock prices
current_prices = {
    "AAPL": 170.00,  # Apple
    "MSFT": 300.00,  # Microsoft
    "GOOGL": 2800.00  # Google
}

# Portfolio dictionary: key is stock symbol (quantity, purchase price)
portfolio = {
    "AAPL": (10, 150.00),  # 10 shares of Apple bought at $150 each
    "MSFT": (5, 250.00),   # 5 shares of Microsoft bought at $250 each
    "GOOGL": (2, 2000.00)  # 2 shares of Google bought at $2000 each
}

# Conversion rate from USD to INR
usd_to_inr = 83.00  # 1 USD = 83 INR

# Function to calculate total portfolio value and profit/loss in INR
def calculate_portfolio(portfolio, current_prices, conversion_rate):
    total_value_inr = 0
    total_profit_loss_inr = 0
    
    print("Stock Portfolio in INR:")
    for stock_symbol, (quantity, purchase_price) in portfolio.items():
        # Get the current price from the dictionary
        current_price = current_prices.get(stock_symbol, 0)
        stock_value = quantity * current_price
        profit_loss = (current_price - purchase_price) * quantity
        
        # Convert values to INR
        stock_value_inr = stock_value * conversion_rate
        profit_loss_inr = profit_loss * conversion_rate
        purchase_price_inr = purchase_price * conversion_rate
        current_price_inr = current_price * conversion_rate

        total_value_inr += stock_value_inr
        total_profit_loss_inr += profit_loss_inr
        
        print(f"{stock_symbol}:")
        print(f"  Quantity: {quantity}")
        print(f"  Purchase Price (INR): ₹{purchase_price_inr:.2f}")
        print(f"  Current Price (INR): ₹{current_price_inr:.2f}")
        print(f"  Current Value (INR): ₹{stock_value_inr:.2f}")
        print(f"  Profit/Loss (INR): ₹{profit_loss_inr:.2f}\n")
    
    print(f"Total Portfolio Value (INR): ₹{total_value_inr:.2f}")
    print(f"Total Profit/Loss (INR): ₹{total_profit_loss_inr:.2f}")

# Run the portfolio tracker
calculate_portfolio(portfolio, current_prices, usd_to_inr)




