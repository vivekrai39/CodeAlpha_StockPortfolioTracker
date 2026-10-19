stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420
}

print("Welcome to Stock Portfolio Tracker!")
print("Available stocks:", stock_prices)

portfolio = {}
total_investment = 0
while True:
    stock_name = input(
        "Enter stock name (AAPL/TSLA/GOOGL/MSFT) or 'done' to finish: "
    ).upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Sorry, stock not found!")
        continue

    quantity = int(input("Enter quantity of shares: "))

    stock_value = stock_prices[stock_name] * quantity

    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
    total_investment += stock_value

    print(f"{stock_name} investment: {stock_value}")

print("\nYour Portfolio:", portfolio)
print("Total Investment:", total_investment)
with open("C:\\Users\\Vivek Rai\\Desktop\\CodeAlpha_StockPortfolioTracker\\portfolio.txt", "w") as file:
    file.write("Stock Portfolio Tracker\n")
    file.write("-----------------------\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity

        file.write(f"Stock: {stock}\n")
        file.write(f"Quantity: {quantity}\n")
        file.write(f"Price: {price}\n")
        file.write(f"Investment: {value}\n\n")

    file.write(f"Total Investment: {total_investment}\n")

print("Portfolio saved successfully in C:\\Users\\Vivek Rai\\Desktop\\CodeAlpha_StockPortfolioTracker\\portfolio.txt")