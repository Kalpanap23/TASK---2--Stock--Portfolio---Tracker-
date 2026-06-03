# Stock Portfolio Tracker

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300,
    "AMZN": 200
}

portfolio = {}
total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")
print("\nAvailable Stocks:")

for stock, price in stocks.items():
    print(f"{stock} : ${price}")

num_stocks = int(input("\nHow many stocks do you want to buy? "))

for i in range(num_stocks):

    stock_name = input("\nEnter Stock Name: ").upper()

    if stock_name not in stocks:
        print("Stock not found!")
        continue

    quantity = int(input("Enter Quantity: "))

    investment = stocks[stock_name] * quantity

    portfolio[stock_name] = {
        "Quantity": quantity,
        "Price": stocks[stock_name],
        "Investment": investment
    }

    total_investment += investment

print("\n===== PORTFOLIO SUMMARY =====")

for stock, details in portfolio.items():

    print(f"""
Stock       : {stock}
Price       : ${details['Price']}
Quantity    : {details['Quantity']}
Investment  : ${details['Investment']}
""")

print(f"\nTOTAL INVESTMENT = ${total_investment}")

# Save into file

with open("portfolio_report.txt", "w") as file:

    file.write("STOCK PORTFOLIO REPORT\n")
    file.write("="*30 + "\n")

    for stock, details in portfolio.items():

        file.write(
            f"{stock} | "
            f"Price: {details['Price']} | "
            f"Qty: {details['Quantity']} | "
            f"Investment: {details['Investment']}\n"
        )

    file.write(f"\nTotal Investment = {total_investment}")

print("\nReport saved successfully!")