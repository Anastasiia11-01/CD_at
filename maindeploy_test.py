from main import app

def test_index():
    assert app.index() == 'Hello, world! You are at farm now'
    #response = requests.get("http://157.230.24.236/")
    #assert response.status_code == 200





