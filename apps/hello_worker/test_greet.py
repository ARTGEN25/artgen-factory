import pytest
from apps.hello_worker.greet import greet

def test_greet_name():
    assert greet("Alice") == "Hello, Alice!"

def test_greet_empty():
    assert greet("") == "Hello, World!"
