def calculate_compound_interest(principal, rate, time, n=1):
    amount = principal * (1 + rate / (100 * n)) ** (n * time)
    return amount - principal


def main():
    print("Compound Interest Calculator")
    print("-" * 30)

    principal = float(input("Enter Principal amount: "))
    rate = float(input("Enter Rate of interest (% per year): "))
    time = float(input("Enter Time period (years): "))
    n = int(input("Enter compounding frequency per year (e.g. 1=yearly, 12=monthly): "))

    interest = calculate_compound_interest(principal, rate, time, n)
    total = principal + interest

    print("-" * 30)
    print(f"Principal:          {principal:>10.2f}")
    print(f"Rate:               {rate:>9.2f}%")
    print(f"Time:               {time:>8.2f} yrs")
    print(f"Compounding:        {n:>10}x/yr")
    print(f"Compound Interest:  {interest:>10.2f}")
    print(f"Total Amount:       {total:>10.2f}")


if __name__ == "__main__":
    main()
