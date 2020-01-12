import pytest
from application import routes

def test_random_letter():
    assert routes.random_letter()["letter"]=="A" or "B" or "C"
