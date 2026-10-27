from unittest.mock import patch

from application.api import hamta_vaderdata


@patch("application.api.requests.get")  #@patch för att ersätta vanliga request.get med en mock
def test_hamta_vaderdata(mock_get): 
    mock_get.return_value.json.return_value = { #fejk data som tas emot

        "latitude":59.33,
        "longitude":18.07,
        "daily": {
            "time": ["2000-01-01"],
            "temperature_2m_mean": [5.0],
            "precipitation_sum": [1.2] 
            }
    }

    mock_get.return_value.raise_for_status.return_value = None # raise_for_status under lyckad anrop ska ge ut värde NONE, annars raise ett felstatus som 404 eller 500.

    data = hamta_vaderdata() #anropar funktion men request.get är fortfarande mockad så inget riktigt anrop ut mot externa API

    mock_get.assert_called_once() #hört att det kan vara bra att kolla att API request bara blev kallad en gång och inte flera.

    # kollar att datan vi får in stämmer överens med vad vi förväntar att få

    assert data is not None
    assert data["latitude"] == 59.33  
    assert data["longitude"] == 18.07 

    assert "latitude" in data  #kollar att viktiga "keys" finns med i json filen.
    assert "longitude" in data
    assert "daily" in data

    assert isinstance(data, dict)  # isinstance kollar om ett värde är just den här typen av data som specifieras i koden. I detta fall data == dict
    assert isinstance(data["latitude"], (int, float))
    assert isinstance(data["daily"]["temperature_2m_mean"], list)

    print("data =", data)
    print("type =", type(data))
  
"""
def test_GET_vader(klient): #kollar igenom om POST response är i rätt format
    svar = klient.get("/api/vader")

    assert svar.status_code == 200
    assert svar.mimetype == "application/json"

    data = svar.get_json()
    assert data["city"] == "Stockholm"
"""