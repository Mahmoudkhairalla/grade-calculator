def print_month_name(month_number):
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    
    if month_number < 1 or month_number > 12:
        return "Invalid month number"
    
    return months[month_number - 1]

def main():
    try:
        month_number = int(input("Enter the number of the month (1-12): "))
        month_name = print_month_name(month_number)
        print(f"The month is: {month_name}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
