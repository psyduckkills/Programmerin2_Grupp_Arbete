import pytest , requests
from app import app

@pytest.fixture
def klient():
    app.config["TESTING"] = True
    return app.test_client()
def test_startsida(klient):
    svar = klient.get("/")
    assert svar.status_code == 200
def test_saknas(klient):
    assert klient.get("/finns-inte").status_code == 404
