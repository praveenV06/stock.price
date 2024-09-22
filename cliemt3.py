# client3.py

# Function to get a data point for the stock
def getDataPoint(stock):
    """Compute the average stock price based on bid and ask prices."""
    stock_name = stock['name']
    bid_price = stock['bid_price']
    ask_price = stock['ask_price']
    
    # Calculate the price as the average of bid and ask prices
    price = (bid_price + ask_price) / 2
    
    # Return a dictionary with stock data
    return {
        'name': stock_name,
        'price': price
    }

# Function to calculate the ratio between two stock prices
def getRatio(price_a, price_b):
    """Return the ratio of price_a to price_b."""
    # Handle division by zero
    if price_b == 0:
        return None
    return price_a / price_b

# Main function to simulate the stock data points and ratio
def main():
    # Example stock list
    stock_list = [
        {'name': 'stock_a', 'bid_price': 100, 'ask_price': 105},
        {'name': 'stock_b', 'bid_price': 200, 'ask_price': 210}
    ]
    
    # Dictionary to store the prices of the stocks
    prices = {}
    
    # Iterate over the stock list to get data points
    for stock in stock_list:
        data_point = getDataPoint(stock)
        prices[stock['name']] = data_point['price']
        
    # Get the ratio between stock_a and stock_b
    ratio = getRatio(prices['stock_a'], prices['stock_b'])
    
    if ratio is not None:
        print(f"The ratio of stock_a to stock_b is: {ratio}")
    else:
        print("Error: Division by zero encountered.")

# Run the main function
if __name__ == "__main__":
    main()
