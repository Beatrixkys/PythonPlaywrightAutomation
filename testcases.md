# Test Cases

## TC-001 – Income Validation

### Scenario

**Given** the user is on the CIMB Personal Loan Calculator
**When** the user enters an income value
**Then** the income should be formatted correctly
**And** the appropriate validation should be applied
**And** the Next button should only be enabled when the income is valid

### Test Data

|   Input | Expected Display | Valid |
| ------: | ---------------: | :---: |
|  199900 |         1,999.00 |   No  |
| -200000 |         2,000.00 |  Yes  |
|   `abc` |             0.00 |   No  |
|       0 |             0.00 |   No  |
|  200000 |         2,000.00 |  Yes  |
|  200001 |         2,000.01 |  Yes  |

### Expected Behaviour

For valid income:

* Income is displayed with the expected formatting.
* The calculator accepts the income.
* The user can proceed to the next step.

For invalid income:

* Income is displayed with the expected formatting.
* The minimum income validation message is displayed.
* The Next button remains disabled.

---

## TC-002 – Loan Amount Validation

### Scenario

**Given** the user has entered a valid income
**When** the user enters a loan amount
**Then** the loan amount should be formatted correctly
**And** the appropriate minimum or maximum validation should be applied
**And** the Next button should only be enabled when the loan amount is valid

### Test Data

|  Input |   Income | Expected Display | Valid |
| -----: | -------: | ---------------: | :---: |
|  `abc` |   200000 |                0 |   No  |
|      0 |   200000 |                0 |   No  |
|   1999 |   200000 |            1,900 |   No  |
|   2000 |   200000 |            2,000 |  Yes  |
| 150001 | 10000000 |          150,000 |  Yes  |
| 300000 | 25000000 |          300,000 |  Yes  |
| 300100 | 25000000 |          300,100 |   No  |

### Expected Behaviour

For valid loan amounts:

* The entered loan amount is displayed correctly.
* The monthly repayment can be calculated.
* The user can proceed to the next step.

For invalid loan amounts:

* The entered value is displayed correctly.
* The appropriate validation message is displayed.
* The Next button remains disabled.

---

## TC-003 – Maximum Loan Amount Based on Income

### Scenario

**Given** the user has entered a valid income
**When** the calculator determines the available loan amount
**Then** the maximum loan amount should be calculated according to the user's income

### Test Data

|   Income | Expected Behaviour                         |
| -------: | ------------------------------------------ |
|   200000 | Maximum loan is calculated based on income |
| 10000000 | Loan amount can be increased to 150,000    |
| 25000000 | Maximum loan is capped at 300,000          |

### Expected Behaviour

The calculator should automatically determine the maximum available loan amount based on the entered income.

---

## TC-004 – Loan Tenure Selection

### Scenario

**Given** the user has entered a valid income and loan amount
**When** the user selects a repayment tenure
**Then** the selected tenure should be displayed correctly
**And** the monthly repayment should be updated accordingly

### Test Data

| Tenure    |
| --------- |
| 24 Months |
| 36 Months |
| 48 Months |
| 60 Months |
| 72 Months |
| 84 Months |

### Expected Behaviour

Each available tenure should be selectable and accepted by the calculator.

---

## TC-005 – Monthly Repayment Calculation

### Scenario

**Given** the user has entered a valid income and loan amount
**And** the user has selected a repayment tenure
**When** the calculator calculates the monthly repayment
**Then** the displayed repayment should match the expected calculation

### Test Data

The repayment calculation is validated using the loan amounts and tenures defined in the automation test data.

The principal amount is rounded down to the nearest 100 before the repayment calculation.

| Input Principal | Principal Used |
| --------------: | -------------: |
|          150010 |         150000 |
|          150099 |         150000 |
|          150100 |         150100 |
|          150199 |         150100 |

### Expected Behaviour

The monthly repayment displayed by the application should match the expected calculated value.

---

## TC-006 – Submit Valid Loan Application

### Scenario

**Given** the user has entered valid calculator details
**When** the user clicks Next
**Then** the user should be navigated to the Lucy application successfully

### Test Data

| Income | Loan Amount | Tenure    |
| -----: | ----------: | --------- |
| 200000 |        2000 | 24 Months |

### Expected Behaviour

* The Next button is enabled.
* Clicking Next navigates to Lucy.
* The Lucy page loads successfully.

---

## TC-007 – Prevent Submission of Invalid Details

### Scenario

**Given** the user has entered invalid calculator details
**When** the validation is triggered
**Then** the appropriate validation message should be displayed
**And** the Next button should remain disabled
**And** the user should not be able to proceed to Lucy

### Covered Data

This scenario is covered by the invalid income and loan amount combinations in TC-001 and TC-002.

---

# Test Coverage Summary

| Test Case | Area                               | Automation |
| --------- | ---------------------------------- | :--------: |
| TC-001    | Income validation                  |     Yes    |
| TC-002    | Loan amount validation             |     Yes    |
| TC-003    | Maximum loan based on income       |     Yes    |
| TC-004    | Loan tenure selection              |     Yes    |
| TC-005    | Monthly repayment calculation      |     Yes    |
| TC-006    | Valid submission / Lucy navigation |     Yes    |
| TC-007    | Invalid submission prevention      |     Yes    |
