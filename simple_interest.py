def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


def main():
    print("Simple Interest Calculator")
    print("-" * 30)

    principal = float(input("Enter Principal amount: "))
    rate = float(input("Enter Rate of interest (% per year): "))
    time = float(input("Enter Time period (years): "))

    interest = calculate_simple_interest(principal, rate, time)
    total = principal + interest

    print("-" * 30)
    print(f"Principal:        {principal:>10.2f}")
    print(f"Rate:             {rate:>9.2f}%")
    print(f"Time:             {time:>8.2f} yrs")
    print(f"Simple Interest:  {interest:>10.2f}")
    print(f"Total Amount:     {total:>10.2f}")


if __name__ == "__main__":
    main()
