import csv
from pathlib import Path
from typing import Type
import pytest
import glaciers
from pytest import raises



file_path_1 = Path(r"C:\Users\ASUS\Desktop\sheet-A.csv")
file_path_2 = Path(r"C:\Users\ASUS\Desktop\sheet-EE.csv")


c = glaciers.GlacierCollection(file_path_1)
c.read_mass_balance_data(file_path_2)

# Test method filter_by_code

# @pytest.mark.parametrize('pattern, code',[('6?3', ['ECHAURREN NORTE', 'SNAEFELL']
# ), ('636', ['ALFA', 'GUANACO']
# ), ('?25', ['CIPRESES', 'PENON']), ('2??', ['CAINHAVARRE'])])

# def test_filter_by_code(pattern, code):
    
#     assert c.filter_by_code(pattern) == code
 

# def test_filter_by_code_imporper_type():
#     with raises(TypeError) as exception: 
#         c.filter_by_code(567) 

# def test_filter_by_code_imporper_value():
#     with raises(ValueError) as exception:
#         c.filter_by_code('9900')
        

# Test method add_mass_balance_value



# Test method sort_by_latest_mass_balance
@pytest.mark.parametrize('n, reverse, object_id',[(5, False, ['01329', '01330', '01328', '02296', '02921']
),(5, True, ['03292', '01316', '03987', '01320', '04532']
), (7, False, ['01329', '01330', '01328', '02296', '02921', '03112', '01319'])])

def test_sort_by_latest_mass_balance(n, reverse, object_id):
    
    assert  [i.id for i in c.sort_by_latest_mass_balance(n, reverse)] == object_id

def test_sort_by_latest_mass_balance_imporper_value():
    with raises(ValueError) as exception:
        c.sort_by_latest_mass_balance(1800, False)


pytest.main(["-s", "test_glaciers.py"])
        
