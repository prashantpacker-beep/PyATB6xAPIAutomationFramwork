import pytest
import allure

@allure.title("Verify that framework is working")
def test_sample_pass():
    assert True == True

@allure.title("Verify that framework is working")
def test_sample_fail():
    assert True == False


