def age_group_classifier(age):
    if age >= 0 and age <= 12:
        return "Child"
    elif age >= 13 and age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"
    else:
        return "Invalid age input"

def main():
    try:
        age = int(input("Enter the person's age: "))
        age_group = age_group_classifier(age)
        print(f"The person belongs to the age group: {age_group}")
    except ValueError:
        print("Invalid input. Please enter a valid age.")

if __name__ == "__main__":
    main()
