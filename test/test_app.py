import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app


@pytest.fixture
def cliente():
    app.config['TESTING'] = True
    with app.test_client() as c:
        yield c

def test_sumar(cliente):
    r = cliente.get('/sumar?a=2&b=3')
    assert r.status_code == 200
    assert r.get_json()['resultado'] == 5

# def test_suma_incorrecta():
#     assert 5 + 2 == 7  # debería ser 7 → falla


