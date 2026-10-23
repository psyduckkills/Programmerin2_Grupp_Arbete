from unittest.mock import patch
from app import TBD #funktions namn som skickar GET request från app.py

@patch("app.request.get")
def test_TBD(mock_get):  #Ändra TBD till funktionens namn
    mock_get.return_value.json.return_value = {

        "exempel": "test"
    }

    resultat = TBD() #Anropar funktionen

    assert resultat == {"exempel": "test"}
    mock_get.assert_called_once_with(
        "https://example.com/user" #skriv in den faktiska URL till externa API
    )
