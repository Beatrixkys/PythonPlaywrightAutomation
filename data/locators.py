# data/locators.py
LOAN_CALC_LOCATORS = {
    # Inputs
    "gross_monthly_income": {
        "strategy": "role",
        "type": "textbox",
        "name": "Gross Monthly Income",
    },

    "loan_amount": {
        "strategy": "role",
        "type": "textbox",
        "name": "Loan Amount",
    },

    # Dropdown
    "loan_tenure": {
        "strategy": "role",
        "type": "combobox",
        "name": "Loan Tenure",
    },

    # Dropdown options
    "tenure_24_months": {
        "strategy": "role",
        "type": "option",
        "name": "24 Months",
    },

    "tenure_36_months": {
        "strategy": "role",
        "type": "option",
        "name": "36 Months",
    },

    # Validation messages
    "minimum_loan_amount_message": {
        "strategy": "text",
        "value": "Minimum loan amount is MYR",
    },

    "maximum_loan_amount_message": {
        "strategy": "text",
        "value": "Maximum loan amount is MYR",
    },

    "minimum_income_message": {
        "strategy": "text",
        "value": "Minimum gross monthly income is MYR",
    },

    # Calculation results
    "monthly_repayment_value": {
        "strategy": "text_parent",
        "text": "Monthly Repayment Amount",
        "child": "h3",
    },

    "interest_rate": {
        "strategy": "text",
        "value": "Interest Rate",
    },

    # Navigation
    "next_button": {
        "strategy": "role",
        "type": "button",
        "name": "Next",
    },
}

LUCY_LOCATORS = {
    "start_heading": {
        "strategy": "role",
        "type": "heading",
        "name": "To start, we need these",
    },
}