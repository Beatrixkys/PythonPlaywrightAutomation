import pytest

from data import params
from pages.loan_calc_page import LoanCalculatorPage
from pages.lucy_page import LucyPage
from verification import verify_loan_calc


@pytest.fixture
def loan_calc_page(page):
    loan_calc_page = LoanCalculatorPage(page)
    loan_calc_page.navigate_loan_page()
    return loan_calc_page


@pytest.fixture
def lucy_page(page):
    return LucyPage(page)


@pytest.mark.loan_calc
@pytest.mark.parametrize("test_data", params.INCOME_TEST_DATA)
def test_income_validation(test_data, loan_calc_page, lucy_page):
    income = test_data["input"]
    valid = test_data["valid"]
    expected = test_data["expected"]
    loan = 2000
    months = "24 Months"

    loan_calc_page.enter_income(income)
    loan_calc_page.enter_loan_amount(loan)
    loan_calc_page.select_tenure(months)

    verify_loan_calc.verify_monthly_repayment(
        loan, months, loan_calc_page.get_monthly_repayment_value()
    )
    
    # Valid income should allow the user to proceed to Lucy
    if valid:
        actual_value = loan_calc_page.get_income_value()
        assert actual_value == expected
        loan_calc_page.click_next()
        lucy_page.is_loaded()
    # Invalid income should display an error and prevent submission
    else:
        actual_value = loan_calc_page.get_income_value()
        assert actual_value == expected
        loan_calc_page.get_error("minimum_income_message")
        assert not loan_calc_page.web_handlers.is_enabled("next_button")


@pytest.mark.loan_calc
@pytest.mark.parametrize("test_data", params.LOAN_TEST_DATA)
def test_loan_amount_validation(test_data, loan_calc_page, lucy_page):
    loan_amount = test_data["input"]
    income = test_data["income"]
    valid = test_data["valid"]
    expected = test_data["expected"]
    months = "24 Months"

    loan_calc_page.enter_income(income)
    # assert calculations of default loan is maxed based on income
    loan_calc_page.assert_max_loan(income)

    loan_calc_page.enter_loan_amount(loan_amount)
    loan_calc_page.select_tenure(months)
    # Valid loan amount should allow the user to proceed to Lucy
    if valid:
        actual_value = loan_calc_page.get_loan_amount()
        verify_loan_calc.verify_monthly_repayment(
            loan_amount, months, 
            loan_calc_page.get_monthly_repayment_value() 
        )
        assert actual_value == expected
        loan_calc_page.click_next()
        lucy_page.is_loaded()
    # Invalid loan amount should display an error and prevent submission
    else:
        actual_value = loan_calc_page.get_loan_amount()
        assert actual_value == expected
        if not isinstance(loan_amount, (int, float)) or loan_amount < 2000:
            loan_calc_page.get_error("minimum_loan_amount_message")
        elif loan_amount > 300000:
            loan_calc_page.get_error("maximum_loan_amount_message")

        assert not loan_calc_page.web_handlers.is_enabled("next_button")


@pytest.mark.loan_calc
@pytest.mark.parametrize("tenure", params.TENURE_TEST_DATA)
def test_tenure_validation(tenure, loan_calc_page, lucy_page):
    income = 200000
    loan_amount = 2000
    loan_calc_page.enter_income(income)
    verify_loan_calc.verify_max_loan(income, loan_calc_page.get_loan_amount())
    loan_calc_page.enter_loan_amount(loan_amount)
    loan_calc_page.select_tenure(tenure)
    # Assert that the monthly repayment 
    # is calculated correctly based on the selected tenure
    verify_loan_calc.verify_monthly_repayment(
        loan_amount, tenure, 
        loan_calc_page.get_monthly_repayment_value()
    )
    loan_calc_page.click_next()
    lucy_page.is_loaded()
