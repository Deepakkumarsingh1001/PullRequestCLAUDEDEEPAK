def compound_interest(principal, rate, time, n=1):
    """
    Calculate compound interest.
    principal: initial amount
    rate: annual interest rate (e.g., 5 for 5%)
    time: time in years
    n: compounding frequency per year (default: 1 = annually)
    """
    amount = principal * (1 + rate / (100 * n)) ** (n * time)
    interest = amount - principal
    return round(amount, 2), round(interest, 2)


if __name__ == "__main__":
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    time = float(input("Enter time (years): "))
    n = int(input("Enter compounding frequency per year (1=annually, 12=monthly, 365=daily): "))

    amount, interest = compound_interest(principal, rate, time, n)

    print(f"\nPrincipal:        ${principal:.2f}")
    print(f"Rate:             {rate}%")
    print(f"Time:             {time} years")
    print(f"Compounded:       {n}x per year")
    print(f"Compound Interest: ${interest:.2f}")
    print(f"Total Amount:     ${amount:.2f}")
