import pytest
from update import merge  # Adjust the import path based on your actual structure

# Test the default behavior without flags
def test_merge_default_behavior():
    orig_data = {"name": "HERE_HERE", "THIS SHOULDNT BE THERE": "A simple example.", "version": 1, "OLDER_VERSION" : 123}
    new_data = { "name": "UPDATED", "version": 555, "features": ["New feature 1", "New feature 2"]}
    expected = {'name': 'UPDATED', 'version': 555, 'features': ['New feature 1', 'New feature 2']}
    merge(orig_data, new_data, force_update=False, full_update=False)
    
    assert orig_data == expected

# Test the force_update behavior
def test_merge_force_update():
    orig_data = {'key1': 'value1', 'key2': 'old_value2'}
    new_data = {'key1': 'THIS SHOULD CHANGE', 'key3': 'value3'}
    expected = {'key1': 'THIS SHOULD CHANGE', 'key2': 'old_value2'}
    merge(orig_data, new_data, force_update=True, full_update= False)

    assert orig_data == expected

# Test the full_update behavior
def test_merge_full_update():
    orig_data = {'key1': 'value1', 'key2': 'old_value2'}
    new_data = {'key2': 'new_value2', 'key3': 'value3'}
    expected = {'key2': 'new_value2', 'key3': 'value3'}
    merge(orig_data, new_data, force_update=False, full_update=True)
    
    assert orig_data == expected

