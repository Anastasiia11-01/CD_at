from main import app
import pytest

def test_index():
    assert main.index() == 'Hello, world! You are at farm now'

def test_cow():
    assert main.cow() == 'MOoooOo!'

def test_dog():
    assert main.dog() == 'Wuff! Wuff!'

def test_cat():
    assert main.cat() == 'MeoooW'
