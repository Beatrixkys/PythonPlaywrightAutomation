## Overview

Automation framework for testing using **Python, Playwright and pytest**.

The tests cover input validation, loan tenure selection, monthly repayment calculation and navigation to the Lucy application flow.

## Application Under Test
https://applynow.cimb.com.my/eform-app/loans/calculator?action=calc&language=en

## Tech Stack

* Python
* Playwright
* pytest
* pytest-html
* Page Object Model (POM)

## Framework Architecture

The framework separates test logic, page-specific actions and common browser interactions.

```text
Tests
  ↓
Page Objects
  ↓
utils/web_handlers.py
  ↓
Playwright
  ↓
Browser
```

### Project Structure

```text
PlaywrightAutomation/
│
├── pages/
│   ├── loan_calc_page.py
│   └── lucy_page.py
│
├── utils/
│   ├── web_handlers.py
│   └── ...
│
├── tests/
│   └── test_loan_calc.py
│
├── params/
│   └── test_data.py
│
├── test_cases/
│   ├── loan_calculator_test_cases.md
│   └── test_data_coverage.md
│
├── reports/
│   └── report.html
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

### Key Components

**`tests/`**
Contains the pytest test scripts and test flow.

**`pages/`**
Contains Page Object classes for interacting with individual application pages.

**`utils/web_handlers.py`**
Common interaction layer used by the Page Objects. It provides reusable browser actions such as locating elements, clicking, filling fields, selecting options and retrieving values.

**`params/`**
Contains test data used for parametrized tests.

**`test_cases/`**
Contains the detailed test cases and test-data coverage separately from the automation code.

**`conftest.py`**
Contains pytest fixtures used to initialise Playwright, the browser and Page Objects.

**`reports/`**
Stores generated test reports.

## Test Flow

The main automation flow is:

1. Open the CIMB Personal Loan Calculator.
2. Validate the calculator input fields.
3. Enter valid and invalid income values.
4. Enter valid and invalid loan amounts.
5. Select each available loan tenure.
6. Validate the monthly repayment.
7. Click **Next**.
8. Verify navigation to the Lucy application flow.

## Test Coverage

The automation currently covers:

* Income field validation
* Loan amount validation
* Loan tenure selection
* Monthly repayment calculation
* Boundary values
* Invalid input values
* Navigation to Lucy
* Parametrized test execution

Detailed test cases and input combinations are maintained separately in the `test_cases/` folder.

## Prerequisites

The following are required before running the tests:

* Python is installed and available from the command line.
* `pip` is available.
* Playwright browser dependencies are installed.
* Internet access is available to access the CIMB application.

Verify Python:

```bash
python --version
```

Verify pip:

```bash
python -m pip --version
```

## Installation

Install the project dependencies:

```bash
python -m pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

## Running the Tests

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

Run all tests:

```bash
pytest
```

Run with the HTML report:

```bash
pytest --html=reports/report.html --self-contained-html
```

Run a specific test file:

```bash
pytest tests/test_loan_calc.py
```

## Test Data

Test data is maintained in:

```text
params/test_data.py
```

pytest parametrization is used to execute the same validation against multiple input values without duplicating test code.

## Reporting

The framework uses `pytest-html` to generate an HTML test report.

Generated reports are stored under:

```text
reports/
```

Example:

```bash
pytest --html=reports/report.html --self-contained-html
```

## Design Approach

The framework uses:

* **Page Object Model** to separate page-specific logic from tests.
* **`web_handlers.py`** to centralise common Playwright interactions.
* **pytest parametrization** to reuse tests with different input data.
* **HTML reporting** to provide a simple execution result that can be shared or reviewed.
