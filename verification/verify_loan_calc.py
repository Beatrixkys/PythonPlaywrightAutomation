import math

import constant


def calculate_monthly_repayment(principal, months):
    if isinstance(months, str):
        months = int(months.lower().replace("months", "").strip())

    years = months / 12
    total_interest = principal * constant.ANNUAL_INTEREST_RATE * years
    total_repayment = principal + total_interest

    return total_repayment / months


def verify_max_loan(income, actual_loan_amount):
    income = income // 100
    expected = min(round(income * 15, -2), 300000)

    assert actual_loan_amount == f"{expected:,}", (
        f"Expected max loan {expected:,}, but got {actual_loan_amount}"
    )


def verify_monthly_repayment(principal, months, actual_repayment):
    principal = (principal // 100) * 100

    expected = math.ceil(calculate_monthly_repayment(principal, months))
    actual = math.ceil(actual_repayment)

    assert actual == expected, (
        f"Expected monthly repayment {expected}, but got {actual}"
    )
