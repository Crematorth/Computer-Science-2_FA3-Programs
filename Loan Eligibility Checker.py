#Gathering User Information for Loan Eligibility
Credit_Score = int(input("Enter your credit score: "))
Annual_Income = int(input("Enter your annual income in dollars: "))
Job_Tenure = int(input("Enter your job tenure in years: "))

#Checking Loan Eligibility
if Credit_Score >= 700 and Annual_Income >= 30000 and Job_Tenure >= 2:
    print("Loan Approved! You are eligible for the loan.")
else:
    print("Loan Denied. You are not eligible for the loan.")