from project import *
import pytest

def test_check_products():
    assert check_products("finish", ["Laptop", "Laptop HP"]) == True
    assert check_products("Laptop", ["Mouse"]) == False
    assert check_products("Laptop", []) == False
    with pytest.raises(SystemExit):
        check_products("finish", []) 



