from playwright.sync_api import Page
from data.locators import LOAN_CALC_LOCATORS
from utils.web_handlers import WebHandlers
import math


class LoanCalculatorPage:

    def __init__(self, page: Page):
        self.page = page
        self.web_handlers = WebHandlers(
            self.page,
            LOAN_CALC_LOCATORS
        )

    def navigate_loan_page(self):
        CIMB_URL = (
            "https://applynow.cimb.com.my/"
            "eform-app/loans/calculator?action=calc"
        )
        self.page.goto(CIMB_URL)

    def enter_income(self, income):
        self.web_handlers.fill(
            "gross_monthly_income",
            income
        )

    def get_income_value(self):
        return self.web_handlers.get_value(
            "gross_monthly_income"
        )

    def enter_loan_amount(self, amount):
        self.web_handlers.fill(
            "loan_amount",
            amount
        )

    def get_loan_amount(self):
        return self.web_handlers.get_value(
            "loan_amount"
        )

    def select_tenure(self, tenure):
        
        self.web_handlers.select(
            "loan_tenure",
            tenure
        )

    def click_next(self):
        assert self.web_handlers.is_enabled("next_button")
        self.web_handlers.click(
            "next_button"
        )

    def get_error(self, field):
        return self.web_handlers.get_text(field)

    def get_monthly_repayment_value(self):
        value = self.web_handlers.get_text(
            "monthly_repayment_value"
        )
        return float(
            value.replace("MYR", "")
                .replace(",", "")
                .strip()
        )

    def get_interest_rate(self):
        return self.web_handlers.get_text(
            "interest_rate"
        )

    def assert_max_loan(self, income):
        income = income // 100
        expected_max_loan = min(round(income * 15, -2), 300000)
        actual_max_loan = self.get_loan_amount()

        assert actual_max_loan == f"{expected_max_loan:,}", (
            f"Expected max loan {expected_max_loan:,}, "
            f"but got {actual_max_loan}")

    def calculate_monthly_repayment(self, principal, months, annual_rate=0.0788):
        if isinstance(months, str):
            months = int(months.lower().replace("months", "").strip())
        years = months / 12
        total_interest = principal * annual_rate * years
        total_repayment = principal + total_interest
        return total_repayment / months

    def assert_monthly_repayment(self, principal, months, annual_rate=0.0788):
        principal = (principal // 100) * 100
        expected_repayment = self.calculate_monthly_repayment(
            principal, months, annual_rate)
        actual_repayment = self.get_monthly_repayment_value()
        expected = math.ceil(expected_repayment)
        actual = int(float(actual_repayment))
        assert actual == expected, (
            f"Expected monthly repayment {expected}, "
            f"but got {actual}"
        )