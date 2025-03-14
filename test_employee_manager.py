# test_employee_manager.py
import datetime
import pytest
from unittest.mock import patch, MagicMock
from employee import Employee
from relations_manager import RelationsManager
from employee_manager import EmployeeManager

@pytest.fixture
def relations_manager():
    return RelationsManager()

@pytest.fixture
def employee_manager(relations_manager):
    return EmployeeManager(relations_manager)

def test_regular_employee_salary(employee_manager):
    """
    Check an employee's salary who is not a team leader whose hire date is 10.10.1998 
    and his base salary is 1000$. Make sure the returned value is 3000$ (1000$ + 20 X 100$).
    """
    # Create a test employee who is not a team leader
    today = datetime.date.today()
    years_employed = 20  # According to the requirement (1000$ + 20 X 100$)
    hire_date = datetime.date(today.year - years_employed, 10, 10)
    
    test_employee = Employee(
        id=100,  # ID that doesn't exist in the teams dictionary
        first_name="Test",
        last_name="Employee",
        birth_date=datetime.date(1980, 1, 1),
        base_salary=1000,
        hire_date=hire_date
    )
    
    # Calculate salary
    salary = employee_manager.calculate_salary(test_employee)
    
    # Expected: base_salary + (years * yearly_bonus)
    expected_salary = 1000 + (years_employed * 100)
    assert salary == expected_salary, f"Expected salary of {expected_salary}$, got {salary}$"

def test_team_leader_salary(employee_manager):
    """
    Check an employee's salary who is a team leader and his team consists of 3 members.
    She was hired on 10.10.2008 and has a base salary of 2000$.
    Validate if the returned value is 3600$ (2000$ + 10 X 100$ + 3 X 200$).
    """
    # Create a mock relations_manager with a custom team leader
    mock_relations_manager = MagicMock()
    
    # Today's date for year calculation
    today = datetime.date.today()
    years_employed = 10  # According to the requirement (2000$ + 10 X 100$ + 3 X 200$)
    hire_date = datetime.date(today.year - years_employed, 10, 10)
    
    # Create test team leader
    team_leader = Employee(
        id=101,
        first_name="Team",
        last_name="Leader",
        birth_date=datetime.date(1975, 5, 15),
        base_salary=2000,
        hire_date=hire_date
    )
    
    # Configure mocks
    mock_relations_manager.is_leader.return_value = True
    mock_relations_manager.get_team_members.return_value = [201, 202, 203]  # 3 team members
    
    # Create employee manager with mock
    custom_employee_manager = EmployeeManager(mock_relations_manager)
    
    # Calculate salary
    salary = custom_employee_manager.calculate_salary(team_leader)
    
    # Expected: base_salary + (years * yearly_bonus) + (team_members * leader_bonus_per_member)
    expected_salary = 2000 + (years_employed * 100) + (3 * 200)
    assert salary == expected_salary, f"Expected salary of {expected_salary}$, got {salary}$"

def test_salary_email_notification(employee_manager):
    """
    Make sure that when you calculate the salary and send an email notification,
    the respective email sender service is used with the correct information.
    """
    # Find an employee to test with
    relations_manager = RelationsManager()
    test_employee = relations_manager.get_all_employees()[0]  # Use the first employee
    
    # Mock the print function to check if it's called with the right message
    with patch('builtins.print') as mock_print:
        # Call the method that sends the notification
        employee_manager.calculate_salary_and_send_email(test_employee)
        
        # Check if print was called with the correct message format
        expected_message = f"{test_employee.first_name} {test_employee.last_name} your salary: {employee_manager.calculate_salary(test_employee)} has been transferred to you."
        mock_print.assert_called_with(expected_message)