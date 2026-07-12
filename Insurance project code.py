print("=== Insurance Fraud Prediction ===\n")

# Main variables
months_as_customer = int(input("Months as Customer: "))
age = int(input("Age: "))
policy_deductable = float(input("Policy Deductible ($): "))
policy_annual_premium = float(input("Policy Annual Premium ($): "))
umbrella_limit = float(input("Umbrella Limit ($): "))
witnesses = int(input("Number of Witnesses: "))
total_claim_amount = float(input("Total Claim Amount ($): "))


# Collision Type
print("\nCollision Type")
print("1. Front Collision")
print("2. Rear Collision")
print("3. Side Collision")
print("4. Unknown")

collision = int(input("Select option: "))

CT_REAR = 1 if collision == 2 else 0
CT_SIDE = 1 if collision == 3 else 0
CT_UNKNOWN = 1 if collision == 4 else 0


# Incident Type
print("\nIncident Type")
print("1. Multi Vehicle")
print("2. Single Vehicle")
print("3. Vehicle Theft")

incident = int(input("Select option: "))

IT_SINGLE = 1 if incident == 2 else 0
IT_THEFT = 1 if incident == 3 else 0


# Incident Severity
print("\nIncident Severity")
print("1. Minor Damage")
print("2. Major Damage")
print("3. Total Loss")
print("4. Trivial Damage")

severity = int(input("Select option: "))

IS_MAJOR = 1 if severity == 2 else 0
IS_TOTAL = 1 if severity == 3 else 0
IS_TRIVIAL = 1 if severity == 4 else 0


# Authorities Contacted
print("\nAuthorities Contacted")
print("1. None")
print("2. Police")
print("3. Fire")
print("4. Ambulance")
print("5. Other")

authority = int(input("Select option: "))

AC_POLICE = 1 if authority == 2 else 0
AC_FIRE = 1 if authority == 3 else 0
AC_AMBULANCE = 1 if authority == 4 else 0
AC_OTHER = 1 if authority == 5 else 0


# Property Damage
print("\nProperty Damage")
print("1. Unknown")
print("2. Yes")
print("3. No")

damage = int(input("Select option: "))

PD_UNKNOWN = 1 if damage == 1 else 0
PD_YES = 1 if damage == 2 else 0
PD_NO = 1 if damage == 3 else 0



print("\n Calculating Fraud Probability...\n")

# Logistic Regression Equation from Rstudio data training results
Equation = (
    -2.772
    + 0.001763 * months_as_customer
    - 0.02284 * age
    + 0.00005995 * policy_deductable
    - 0.0001762 * policy_annual_premium
    + 0.00000009979 * umbrella_limit
    + 0.3019 * CT_REAR
    - 0.1702 * CT_SIDE
    + 0.9798 * CT_UNKNOWN
    + 0.1794 * IT_SINGLE
    - 0.2424 * IT_THEFT
    + 2.630 * IS_MAJOR
    + 0.2365 * IS_TOTAL
    - 0.6974 * IS_TRIVIAL
    + 0.7293 * AC_POLICE
    + 0.5889 * AC_FIRE
    + 0.7714 * AC_AMBULANCE
    + 1.006 * AC_OTHER
    - 0.3136 * PD_NO
    + 0.07627 * witnesses
    + 0.000003721 * total_claim_amount
)
#bringing it out of log odds
Final_Probability = 1 / (1 + 2.718281828459045235360287471352**(-Equation))
#final output
print(f"Fraud Probability: {Final_Probability:.2%}")











