INCOME_TEST_DATA = [
    {
        "input": 199900,
        "expected": "1,999.00",
        "valid": False,
    },
    {
        "input": -200000,
        "expected": "2,000.00",
        "valid": True,
    },
    {
        "input": "abc",
        "expected": "0.00",
        "valid": False,
    },
    {
        "input": 0000,
        "expected": "0.00",
        "valid": False,
    },
    {
        "input": 200000,
        "expected": "2,000.00",
        "valid": True,
    },
    {
        "input": 200001,
        "expected": "2,000.01",
        "valid": True,
    },
]

LOAN_TEST_DATA = [
    {
        "input": "abc",
        "income": 200000,
        "expected": "0",
        "valid": False,
    },
    {
        "input": 0000,
        "income": 200000,
        "expected": "0",
        "valid": False,
    },
    {
        "input": 1999,
        "income": 200000,
        "expected": "1,900",
        "valid": False,
    },
    {
        "input": 2000,
        "income": 200000,
        "expected": "2,000",
        "valid": True,
    },
    {
        "input": 150001,
        "income": 10000000,
        "expected": "150,000",
        "valid": True,
    },
    {
        "input": 300000,
        "income": 25000000,
        "expected": "300,000",
        "valid": True,
    },
    {
        "input": 300100,
        "income": 25000000,
        "expected": "300,100",
        "valid": False,
    },
]

TENURE_TEST_DATA = [
    "24 Months",
    "36 Months",
    "48 Months",
    "60 Months",
    "72 Months",
    "84 Months",
]
