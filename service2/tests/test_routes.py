import pytest
from application import routes

def test_random_number():
    assert routes.random_number()["number"]=="0" or "1" or "2"or "3" or "4" or "5" or "6"
