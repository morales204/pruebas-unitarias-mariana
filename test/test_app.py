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

def test_restar(cliente):
    r = cliente.get('/restar?a=10&b=4')
    assert r.status_code == 200
    assert r.get_json()['resultado'] == 6

def test_multiplicar(cliente):
    r = cliente.get('/multiplicar?a=3&b=5')
    assert r.status_code == 200
    assert r.get_json()['resultado'] == 15

def test_dividir(cliente):
    r = cliente.get('/dividir?a=10&b=2')
    assert r.status_code == 200
    assert r.get_json()['resultado'] == 5

def test_dividir_por_cero(cliente):
    r = cliente.get('/dividir?a=10&b=0')
    assert r.status_code == 400
    assert 'error' in r.get_json()

def test_sumar_negativos(cliente):
    r = cliente.get('/sumar?a=-5&b=-3')
    assert r.status_code == 200
    assert r.get_json()['resultado'] == -8