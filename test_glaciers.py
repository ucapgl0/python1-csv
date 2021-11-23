from pathlib import Path
from typing import Type
import pytest
import glaciers
from pytest import raises



file_path_1 = Path(r"C:\Users\ASUS\Desktop\sheet-A.csv")
file_path_2 = Path(r"C:\Users\ASUS\Desktop\sheet-EE.csv")


c = glaciers.GlacierCollection(file_path_1)
c.read_mass_balance_data(file_path_2)
g = glaciers.Glacier


# Test method add_mass_balance_value
@pytest.mark.parametrize('self_measurement, year, value, boolean, expect',[({}, 2010, 800, False, {2010: 800}),
 ({2010: 250}, 2010, 300, False, {2010:250}),
({2009: 250}, 2010, 250, True, {2009: 250, 2010: 250}),
({2011: 250, 2012: 600}, 2012, 250, True, {2011: 250, 2012: 850})])

def test_add_mass_balance_measurement(self_measurement, year, value, boolean, expect):
    
    g.add_mass_balance_measurement(self_measurement, year, value, boolean)   
    assert  self_measurement == expect
    # In second test, self_measurement could change the input value as output in the first test when boolean == True
    # Therefore, in order to pass the second test, we need to get new expect value
    g.add_mass_balance_measurement(expect, year, value, boolean)



# Test method filter_by_code
@pytest.mark.parametrize('pattern, code',[('6?3', ['ECHAURREN NORTE', 'SNAEFELL']
), ('636', ['ALFA', 'GUANACO']
), ('?25', ['CIPRESES', 'PENON']), ('2??', ['CAINHAVARRE'])])

def test_filter_by_code(pattern, code):
    
    assert c.filter_by_code(pattern) == code
 

def test_filter_by_code_imporper_type():
    with raises(TypeError) as exception: 
        c.filter_by_code(567) 

def test_filter_by_code_imporper_type_2():
    with raises(TypeError) as exception:
        c.filter_by_code('6a3')

def test_filter_by_code_imporper_value_1():
    with raises(ValueError) as exception:
        c.filter_by_code('6600')

       

# Test method sort_by_latest_mass_balance
@pytest.mark.parametrize('n, reverse, object_id',[(5, False, ['01329', '01330', '01328', '02296', '02921']
),(5, True, ['03292', '01316', '03987', '01320', '04532']
), (7, False, ['01329', '01330', '01328', '02296', '02921', '03112', '01319'])])

def test_sort_by_latest_mass_balance(n, reverse, object_id):
    
    assert  [i.id for i in c.sort_by_latest_mass_balance(n, reverse)] == object_id

def test_sort_by_latest_mass_balance_imporper_value():
    with raises(ValueError) as exception:
        c.sort_by_latest_mass_balance(1800, False)


pytest.main(["test_glaciers.py"])
        
