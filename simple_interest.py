def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


def calculate_compound_interest(principal, rate, time, n=1):
    amount = principal * (1 + rate / (100 * n)) ** (n * time)
    return amount - principal


def main():
    print("Interest Calculator")
    print("-" * 30)

    principal = float(input("Enter Principal amount: "))
    rate = float(input("Enter Rate of interest (% per year): "))
    time = float(input("Enter Time period (years): "))

    si = calculate_simple_interest(principal, rate, time)
    n = int(input("Enter compounding frequency per year (e.g. 1=yearly, 12=monthly): "))
    ci = calculate_compound_interest(principal, rate, time, n)

    print("-" * 30)
    print(f"Principal:          {principal:>10.2f}")
    print(f"Rate:               {rate:>9.2f}%")
    print(f"Time:               {time:>8.2f} yrs")
    print(f"Simple Interest:    {si:>10.2f}")
    print(f"SI Total Amount:    {principal + si:>10.2f}")
    print("-" * 30)
    print(f"Compounding:        {n:>10}x/yr")
    print(f"Compound Interest:  {ci:>10.2f}")
    print(f"CI Total Amount:    {principal + ci:>10.2f}")


if __name__ == "__main__":
    main()
