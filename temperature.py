def classify_temperature(temp):
    if temp < 0:
        return "Freezing"
    elif temp < 10:
        return "Very Cold"
    elif temp < 20:
        return "Cold"
    elif temp < 30:
        return "Moderate"
    elif temp < 40:
        return "Hot"
    else:
        return "Very Hot"

def main():
    try:
        temperature = float(input("Enter the temperature in Celsius: "))
        classification = classify_temperature(temperature)
        print(f"The temperature is classified as: {classification}")
    except ValueError:
        print("Invalid input. Please enter a numeric value for temperature.")

if __name__ == "__main__":
    main()
