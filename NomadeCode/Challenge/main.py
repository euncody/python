# 👇🏻 YOUR CODE 👇🏻:

# 연간 매출 계산
def get_yearly_revenue(monthly_revenue):
    return monthly_revenue * 12

# 연간 비용 계산
def get_yearly_expenses(monthly_expenses):
    return monthly_expenses * 12

# 세금 계산
def get_tax_amount(profit):
    if profit > 100000:
        tax_rate = 0.25
    else:
        tax_rate = 0.15
    return profit * tax_credits

# 세액 공제 적용
def apply_tax_credits(tax_amount, tax_credit):
    return profit * tax_credits

# /YOUR CODE

# BLUEPRINT | DONT EDIT

monthly_revenue = 5500000
monthly_expenses = 2700000
tax_credits = 0.01

yearly_revenue = get_yearly_revenue(monthly_revenue)
yearly_expenses = get_yearly_expenses(monthly_expenses)

profit = yearly_revenue - yearly_expenses

tax_amount = get_tax_amount(profit)

final_tax_amount = tax_amount - apply_tax_credits(tax_amount, tax_credits)

print(f"Your tax bill is: ${final_tax_amount}")

# /BLUEPRINT
