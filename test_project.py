from project import *
import pytest

def test_check_products():
    
    assert check_products("finish", ["Laptop", "Laptop HP"]) == True
    assert check_products("Laptop", ["Mouse"]) == False
    assert check_products("Laptop", []) == False
    with pytest.raises(SystemExit):
        check_products("finish", []) 

def test_format_stores():
    
    with pytest.raises(SystemExit):
        format_stores({"amazon": "n", "ml": "n"})

    assert type(format_stores({"amazon": "y", "ml": "n"})[0]) == type(mysites.Amazon())
    assert type(format_stores({"amazon": "n", "ml": "y"})[0]) == type(mysites.ML())
    
    assert len(format_stores({"amazon": "y", "ml": "y"})) == 2
    assert type(format_stores({"amazon": "y", "ml": "y"})[0]) == type(mysites.Amazon())
    assert type(format_stores({"amazon": "y", "ml": "y"})[1]) == type(mysites.ML())

def test_excel_name():
    
    assert excel_name(["Laptop", "Laptop HP"]) == "Laptop.xlsx"
    assert excel_name(["Box", "Small Box", "Big Box"]) == "Box.xlsx"
    assert excel_name(["Smartphone", "Iphone", "Xiaomi"]) == "Smartphone.xlsx"

def test_post_scrapper():
    
    assert post_scrapper("test_excel.xlsx") == True

    
