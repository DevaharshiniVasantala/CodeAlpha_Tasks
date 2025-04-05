import yfinance as yf

class StockPortfolioTracker:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, quantity, buy_price):
        symbol = symbol.upper()
        self.portfolio[symbol] = {
            "quantity": quantity,
            "buy_price": buy_price
        }
        print(f"Added {symbol} to portfolio.")

    def remove_stock(self, symbol):
        symbol = symbol.upper()
        if symbol in self.portfolio:
            del self.portfolio[symbol]
            print(f"Removed {symbol} from portfolio.")
        else:
            print("Stock not found.")

    def show_portfolio(self):
        if not self.portfolio:
            print("Your portfolio is empty.")
            return

        print("\nCurrent Portfolio:")
        print("-" * 60)
        total_value = 0
        total_invested = 0

        for symbol, data in self.portfolio.items():
            stock = yf.Ticker(symbol)
            try:
                current_price = stock.history(period="1d")['Close'].iloc[-1]
            except Exception as e:
                print(f"Failed to fetch data for {symbol}: {e}")
                continue

            quantity = data["quantity"]
            buy_price = data["buy_price"]
            invested = quantity * buy_price
            value = quantity * current_price
            profit = value - invested

            total_value += value
            total_invested += invested

            print(f"{symbol}:")
            print(f"  Quantity: {quantity}")
            print(f"  Buy Price: ${buy_price:.2f}")
            print(f"  Current Price: ${current_price:.2f}")
            print(f"  Value: ${value:.2f}")
            print(f"  Profit/Loss: ${profit:.2f}")
            print("-" * 60)

        print(f"Total Invested: ${total_invested:.2f}")
        print(f"Total Current Value: ${total_value:.2f}")
        print(f"Overall Profit/Loss: ${total_value - total_invested:.2f}")

def main():
    tracker = StockPortfolioTracker()

    while True:
        print("\n1. Add Stock")
        print("2. Remove Stock")
        print("3. Show Portfolio")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            symbol = input("Enter stock symbol (e.g., AAPL): ")
            quantity = int(input("Enter quantity: "))
            buy_price = float(input("Enter buy price: "))
            tracker.add_stock(symbol, quantity, buy_price)

        elif choice == "2":
            symbol = input("Enter stock symbol to remove: ")
            tracker.remove_stock(symbol)

        elif choice == "3":
            tracker.show_portfolio()

        elif choice == "4":
            print("Exiting portfolio tracker.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()