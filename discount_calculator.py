def calculate_total_cost(amount):
    if amount > 100:
        discount = amount * 0.10
    elif amount > 50:
        discount = amount * 0.05
    else:
        discount = 0
    
    total_cost = amount - discount
    return total_cost

def main():
    try:
        amount = float(input("Enter the purchase amount ($): "))
        if amount < 0:
            print("Invalid input. Purchase amount cannot be negative.")
            return
        
        total_cost = calculate_total_cost(amount)
        print(f"Total cost after discount: ${total_cost:.2f}")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the purchase amount.")

if __name__ == "__main__":
    main()
