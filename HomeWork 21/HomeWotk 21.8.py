import math


def compound_interest(principal, rate, times_compounded, years):
    """
    Calculate compound interest.
    """
    return principal * (1 + rate / times_compounded) ** (times_compounded * years)

def loan_payment(principal, annual_rate, periods):
    """
    Calculate monthly loan payment.
    """
    monthly_rate = annual_rate / 12 / 100
    return principal * monthly_rate / (1 - math.pow(1 + monthly_rate, -periods))

def investment_return(principal, annual_rate, years):
    """
    Calculate future value of an investment.
    """
    return principal * (1 + annual_rate / 100) ** years

financial_functions = {
    'compound': compound_interest,
    'loan': loan_payment,
    'investment': investment_return
}


def financial_calculator(operation, **kwargs):
    if operation in financial_functions:
        return financial_functions[operation](**kwargs)
        

   
operator = input("Write (compound, loan, investment):\t").lower()


if operator == "compound":
    principal = float(input("Write a principal:\t"))
    rate = float(input("Write a rate:\t"))
    times_compounded = int(input("Write a times compounded:\t"))
    years = float(input("Write a year:\t"))
    
    fin_cal = financial_calculator("compound", principal=principal, rate=rate, times_compounded=times_compounded, years=years)

    print(f"Compound interest result: ${fin_cal:.2f}")
    
elif operator == "loan":
    principal = float(input("Write a principal:\t"))
    annual_rate = float(input("Write a annual rate:\t"))
    periods = float(input("Write a periods:\t"))
    
    fin_cal = financial_calculator('loan', principal=principal, annual_rate=annual_rate, periods=periods)
    
    print(f"Loan interest result: ${fin_cal:.2f}")
    
elif operator == "investment":
    principal = float(input("Write a principal:\t"))
    annual_rate = float(input("Write a annual rate:\t"))
    years = float(input("Write a years:\t"))
    
    fin_cal = financial_calculator('investment', principal=principal, annual_rate=annual_rate, years=years) 
    
    print(f"Investment interest result: ${fin_cal:.2f}")
    
else:
    print("Operator not found!")