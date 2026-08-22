# Equal Expense Split Calculator
# Define expenses for each person
expenses = {
    'Person A': [20, 30, 40],
    'Person B': [60, 70],
    'Person C': [10, 20, 40]
}

# Calculate total spent by each person
print("=" * 50)
print("EXPENSE SPLIT CALCULATOR")
print("=" * 50)
print("\nIndividual Expenses:")
person_totals = {}
total_expenses = 0

for person, expenses_list in expenses.items():
    total = sum(expenses_list)
    person_totals[person] = total
    total_expenses += total
    print(f"{person}: {expenses_list} = ${total}")

# Calculate average per person
num_people = len(expenses)
average_per_person = total_expenses / num_people

print(f"\nTotal Expenses: ${total_expenses}")
print(f"Number of People: {num_people}")
print(f"Average per Person: ${average_per_person:.2f}")

# Calculate how much each person owes or is owed
print("\n" + "=" * 50)
print("SETTLEMENT:")
print("=" * 50)

settlements = {}
for person, spent in person_totals.items():
    balance = spent - average_per_person
    settlements[person] = balance
    if balance > 0:
        print(f"{person} paid ${spent:.2f}, owes back: ${balance:.2f}")
    elif balance < 0:
        print(f"{person} paid ${spent:.2f}, needs to pay: ${abs(balance):.2f}")
    else:
        print(f"{person} paid ${spent:.2f}, is even!")

# Show who pays whom
print("\n" + "=" * 50)
print("WHO PAYS WHOM:")
print("=" * 50)

debtors = {p: abs(b) for p, b in settlements.items() if b < 0}  # Need to pay
creditors = {p: b for p, b in settlements.items() if b > 0}     # Owed money

for debtor, debt_amount in debtors.items():
    print(f"\n{debtor} needs to pay ${debt_amount:.2f}:")
    remaining_debt = debt_amount
    
    for creditor, credit_amount in creditors.items():
        if remaining_debt <= 0:
            break
        payment = min(remaining_debt, credit_amount)
        print(f"  -> Pay {creditor}: ${payment:.2f}")
        remaining_debt -= payment
        creditors[creditor] -= payment