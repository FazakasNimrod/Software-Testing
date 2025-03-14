# test_relations_manager.py
import datetime
import pytest
from relations_manager import RelationsManager
from employee import Employee

# Setup fixture to reuse RelationsManager across tests
@pytest.fixture
def relations_manager():
    return RelationsManager()

def test_john_doe_is_team_leader_with_correct_birthdate(relations_manager):
    """Check if there is a team leader called John Doe whose birthdate is 31.01.1970."""
    # Find John Doe in the employee list
    john_doe = next((emp for emp in relations_manager.get_all_employees() 
                     if emp.first_name == "John" and emp.last_name == "Doe"), None)
    
    # Assert John Doe exists, is a team leader, and has the correct birthdate
    assert john_doe is not None, "John Doe should exist in the employee list"
    assert relations_manager.is_leader(john_doe), "John Doe should be a team leader"
    assert john_doe.birth_date == datetime.date(1970, 1, 31), "John Doe's birthdate should be 31.01.1970"

def test_john_doe_team_members(relations_manager):
    """Check if John Doe's team members are Myrta Torkelson and Jettie Lynch."""
    # Find John Doe
    john_doe = next((emp for emp in relations_manager.get_all_employees() 
                    if emp.first_name == "John" and emp.last_name == "Doe"), None)
    
    # Get John's team members (should now be Employee objects, not IDs)
    team_members = relations_manager.get_team_members(john_doe)
    
    # Check if Myrta and Jettie are in John's team
    myrta = next((emp for emp in team_members 
                 if emp.first_name == "Myrta" and emp.last_name == "Torkelson"), None)
    jettie = next((emp for emp in team_members 
                  if emp.first_name == "Jettie" and emp.last_name == "Lynch"), None)
    
    assert myrta is not None, "Myrta Torkelson should be in John Doe's team"
    assert jettie is not None, "Jettie Lynch should be in John Doe's team"
    assert len(team_members) == 2, "John Doe should have exactly 2 team members"

def test_tomas_andre_not_in_john_doe_team(relations_manager):
    """Make sure that Tomas Andre is not John Doe's team member."""
    # Find John Doe and Tomas Andre
    john_doe = next((emp for emp in relations_manager.get_all_employees() 
                    if emp.first_name == "John" and emp.last_name == "Doe"), None)
    tomas_andre = next((emp for emp in relations_manager.get_all_employees() 
                       if emp.first_name == "Tomas" and emp.last_name == "Andre"), None)
    
    # Get John's team member IDs
    team_member_ids = relations_manager.get_team_members(john_doe)
    
    assert tomas_andre.id not in team_member_ids, "Tomas Andre should not be in John Doe's team"

def test_gretchen_walford_salary(relations_manager):
    """Check if Gretchen Walford's base salary equals 4000$."""
    # Find Gretchen Walford
    gretchen = next((emp for emp in relations_manager.get_all_employees() 
                    if emp.first_name == "Gretchen" and emp.last_name == "Watford"), None)
    
    assert gretchen is not None, "Gretchen Walford should exist in the employee list"
    assert gretchen.base_salary == 4000, "Gretchen Walford's base salary should be 4000$"

def test_tomas_andre_not_team_leader(relations_manager):
    """Make sure Tomas Andre is not a team leader. Check what happens if you try to retrieve his team members."""
    # Find Tomas Andre
    tomas_andre = next((emp for emp in relations_manager.get_all_employees() 
                       if emp.first_name == "Tomas" and emp.last_name == "Andre"), None)
    
    assert not relations_manager.is_leader(tomas_andre), "Tomas Andre should not be a team leader"
    
    # Check what happens when trying to get team members for a non-leader
    team_members = relations_manager.get_team_members(tomas_andre)
    assert team_members == [], "Getting team members for a non-leader should return an empty list"

def test_jude_overcash_not_in_database(relations_manager):
    """Make sure that Jude Overcash is not stored in the database."""
    # Check if anyone named Jude Overcash exists in employee list
    jude_overcash = next((emp for emp in relations_manager.get_all_employees() 
                         if emp.first_name == "Jude" and emp.last_name == "Overcash"), None)
    
    assert jude_overcash is None, "Jude Overcash should not exist in the employee list"