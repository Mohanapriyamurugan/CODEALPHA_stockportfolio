portfolio = {}
def add_stock():
    name = input("Enter Stock Name: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price per Stock: "))
    total_value = quantity * price
    portfolio[name] = {'quantity': quantity, 'price': price, 'total': total_value}
    print(f"\n{name} added to portfolio!\n")
def display_portfolio():
    if not portfolio:
        print("\nPortfolio is empty.\n")
        return
    print("\nCurrent Portfolio:")
    for name, data in portfolio.items():
        print(f"Stock: {name}, Quantity: {data['quantity']}, Price: ₹{data['price']}, Total: ₹{data['total']}")
    print()
def save_portfolio():
    with open("portfolio.txt", "w") as file:
        for name, data in portfolio.items():
            file.write(f"{name},{data['quantity']},{data['price']},{data['total']}\n")
    print("\nPortfolio saved to 'portfolio.txt'\n")
def load_portfolio():
    try:
        with open("portfolio.txt", "r") as file:
            for line in file:
                name, quantity, price, total = line.strip().split(",")
                portfolio[name] = {
                    'quantity': int(quantity),
                    'price': float(price),
                    'total': float(total)
                }
        print("\nPortfolio loaded from 'portfolio.txt'\n")
    except FileNotFoundError:
        print("\nNo saved portfolio found.\n")
while True:
    print("1. Add Stock")
    print("2. Display Portfolio")
    print("3. Save Portfolio")
    print("4. Load Portfolio")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_stock()
    elif choice == '2':
        display_portfolio()
    elif choice == '3':
        save_portfolio()
    elif choice == '4':
        load_portfolio()
    elif choice == '5':
        print("\nExiting Program. Thank you!\n")
        break
    else:
        print("\nInvalid Choice. Try Again!\n")