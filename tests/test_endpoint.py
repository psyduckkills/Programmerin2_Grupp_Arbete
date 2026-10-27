import pytest

from app import app


@pytest.fixture  
def klient(): 
    app.config["TESTING"] = True   #skapar en klient med flasks testing fas aktiverad. 
    return app.test_client()       #skickar requests utan att starta en web server. Den kollar om responsen 

def test_startsida_finns(klient):
    svar = klient.get("/")           #kollar om klienten får startsidan
    assert svar.status_code == 200   #assert kollar om något är sant. I detta fall, kollar den om klienten får status koden lika med 200.

def test_saknas_endpoint(klient):    #@app.errorhandler(404) finns i app.py som gör att vår 404.html sida visas under 404 fel
    svar = klient.get("/finns-inte")

    assert svar.status_code == 404   #kollar om endpoint /finns-inte ger http status kod 404.
    assert b"Page not Found 404" in svar.data #kollar att "Page not Found 404" finns i html data i vår 404.html. b sträng används när svaret är av typen byte.

