from main import app

def test_index():
    url = 'http://157.230.24.236/'
    resp = requests.get(url)
    assert resp.status_code == 200


