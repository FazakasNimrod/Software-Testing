# Software Testing Project with pytest

![Python](https://img.shields.io/badge/Python-3.x-blue)
![pytest](https://img.shields.io/badge/pytest-8.x-green)
![Tests](https://github.com/FazakasNimrod/Software-Testing/actions/workflows/pytest.yml/badge.svg)

## 📋 Overview

This repository contains a comprehensive suite of unit tests for an employee management system, implemented using pytest. The project demonstrates software testing best practices by thoroughly testing the functionality of a simple employee management application with classes for employee data, team management, and salary calculations.

## 🏗️ Project Structure

```
.
├── calculator.py                # Simple calculator example
├── calculator_test.py           # Tests for calculator example
├── employee.py                  # Employee class definition
├── employee_manager.py          # Salary calculation and notification
├── relations_manager.py         # Team management functionality
├── requirements.txt             # Project dependencies
├── test_employee_manager.py     # Tests for EmployeeManager
└── test_relations_manager.py    # Tests for RelationsManager
```

## ✨ Features

- **Comprehensive Unit Testing**: Complete test coverage for all key functions
- **Test Fixtures**: Reusable test components for consistent testing
- **Mock Objects**: Simulated objects for isolated testing
- **Assertion Messages**: Clear feedback when tests fail

## 🧪 Test Cases

### RelationsManager Tests

1. Verify team leader identification (John Doe)
2. Check team membership (Myrta Torkelson and Jettie Lynch)
3. Confirm non-membership (Tomas Andre not in John Doe's team)
4. Validate employee base salary (Gretchen Walford)
5. Test invalid operations (Tomas Andre not a team leader)
6. Verify database integrity (Jude Overcash not in database)

### EmployeeManager Tests

1. Calculate regular employee salary with appropriate years of service
2. Calculate team leader salary with team size bonuses
3. Verify email notification functionality

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Virtual environment (recommended)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/Software-Testing.git
   cd Software-Testing
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv pytest-env
   source pytest-env/bin/activate  # On Windows: pytest-env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running Tests

Run all tests:

```bash
pytest -v
```

Run specific test file:

```bash
pytest -v test_relations_manager.py
```

## 📝 Development Process

This project follows a systematic approach to unit testing:

1. **Understanding Requirements**: Analyze what needs to be tested
2. **Test Design**: Create test cases that cover edge cases and typical usage
3. **Test Implementation**: Write clear and maintainable test code
4. **Execution**: Run tests systematically to identify issues
5. **Refinement**: Update tests as code changes

## 🔍 Key Testing Concepts Demonstrated

- **Unit Testing**: Testing individual components in isolation
- **Test Fixtures**: Setting up consistent test environments
- **Mocking**: Simulating components to isolate what's being tested
- **Edge Cases**: Testing boundary conditions and error scenarios
- **Assertions**: Validating expected behaviors

## 📚 Resources

- [pytest Documentation](https://docs.pytest.org/)
- [Python Unit Testing Best Practices](https://realpython.com/python-testing/)
- [Software Testing Fundamentals](https://softwaretestingfundamentals.com/)
