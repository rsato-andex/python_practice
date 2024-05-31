import requests

def test_hello_world():
    response = requests.get('http://pptest_python:8000')
    assert response.status_code == 200
    assert response.text == "<a href='http://localhost:8001/top'>TOP</a>"

def test_top():
    response = requests.get('http://localhost:8000/top')
    assert response.status_code == 2000
    assert response.text == "top"

if __name__ == '__main__':
    test_hello_world()
