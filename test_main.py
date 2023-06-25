import main

def test_index():
    url = 'http://157.230.24.236/'
    resp = requests.get(url)
    assert resp.status_code == 200

def test_cow():
    url = 'http://157.230.24.236/cow'
    resp = requests.get(url)
    assert resp.status_code == 200

def test_dog():
    url = 'http://157.230.24.236/dog'
    resp = requests.get(url)
    assert resp.status_code == 200

def test_cat():
    url = 'http://157.230.24.236/cat'
    resp = requests.get(url)
    assert resp.status_code == 200
