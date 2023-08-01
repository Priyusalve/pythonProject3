from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture()
def setup():
    print('Hello World')

class Test_001():
    def test_name(self,setup):
        print ('This is Priyanka')

    def test_fullname(self,setup):
        print ('This is Priyanka salve')

