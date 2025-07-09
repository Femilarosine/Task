# Hardcoded dictionary with stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 130,
    "MSFT": 320,
    "AMZN": 125
}

portfolio = {}
total_investment = 0

print("Welcome to the Stock Portfolio Tracker")
print("Available stocks:", ', '.join(stock_prices.keys()))

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not found in price list. Try again.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        if quantity < 0:
            print("Quantity cannot be negative.")
            continue
    except ValueError:
        print("Please enter a valid number for quantity.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity
    print(f"Added {quantity} shares of {stock} to portfolio.\n")

# Calculate total investment
print("\nYour Portfolio Summary:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_investment += value
    print(f"{stock}: {quantity} shares x ${price} = ${value}")

print(f"\nTotal Investment Value: ${total_investment}")

# Optional: Save to file
save = input("Would you like to save this to a file? (yes/no): ").lower()
if save == 'yes':
    filename = "portfolio_summary.txt"
    with open(filename, "w") as file:
        file.write("Portfolio Summary:\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity
            file.write(f"{stock}: {quantity} shares x ${price} = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}")
    print(f"Portfolio saved to {filename}")
