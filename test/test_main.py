import pytest
import os
from src.main import Main

# https://stackoverflow.com/questions/17801300/how-to-run-a-method-before-all-tests-in-all-classes
@pytest.fixture(scope="session", autouse=True)
def set_varaible_env():
    os.environ["HOST"] = "test"
    os.environ["TOKEN"] = "test"
    os.environ["TICKETS"] = "test"
    os.environ["T_MAX"] = "test"
    os.environ["T_MIN"] = "test"
    os.environ["DATABASE"] = "test"
    assert True

def test_variable_env():
    assert "test" == os.environ.get("HOST")
    assert "test" == os.environ.get("TOKEN")
    assert "test" == os.environ.get("TICKETS")
    assert "test" == os.environ.get("T_MAX")
    assert "test" == os.environ.get("T_MIN")
    assert "test" == os.environ.get("DATABASE")

def test_variables_defaut():
    del os.environ["HOST"]
    del os.environ["TOKEN"]
    del os.environ["TICKETS"]
    del os.environ["T_MAX"]
    del os.environ["T_MIN"]
    del os.environ["DATABASE"]
    main = Main()
    assert main.HOST == "http://34.95.34.5"
    assert main.TOKEN == "Default"
    assert main.TICKETS == 10
    assert main.T_MAX == 100 
    assert main.T_MIN == 0
    assert main.DATABASE == "Default"