import main

def test_index():
    assert main.index() == 'Assignment done once again!'
    #response = requests.get("http://157.230.24.236/")
    #assert response.status_code == 200

def test_index():
    assert main.index() == 'Hello, world! You are at farm now'

def test_cow():
    assert main.cow() == 'MOoooOo!'

def test_dog():
    assert main.dog() == 'Wuff! Wuff!'

def test_cat():
    assert main.cat() == 'MeoooW





