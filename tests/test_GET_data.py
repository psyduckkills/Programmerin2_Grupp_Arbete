from unittest.mock import patch

from application.api import hamta_vaderdata


@patch(
    "application.api.requests.get"
)  # @patch används för att ersätta vanliga request.get med en mock
def test_mock_requests_get(
    mock_get,
):  # mock_get är en mock av requests.get som används i hamta_vaderdata

    # fejk response data som vår get.request får från mocken istället för externa API:et.
    mock_get.return_value.json.return_value = {
        "latitude": 59.33,
        "longitude": 18.07,
        "daily": {
            "time": ["2000-01-01"],
            "temperature_2m_mean": [5.0],
            "precipitation_sum": [1.2],
        },
    }

    # 2. raise_for_status under lyckad anrop (HTTP status 200) ska ge ut värde NONE, annars raise ett felstatus som t.ex 404 eller 500.

    mock_get.return_value.raise_for_status.return_value = None

    # 3. anropar funktion men request.get är fortfarande mockad så inget riktigt anrop ut mot externa API

    data = hamta_vaderdata()

    # 4. kolla att API request bara blev kallad en gång och med "with" i slutet av koden så kan du testa att din requests.get skickar rätt data som du förväntade dig.
    mock_get.assert_called_once_with(
        "https://archive-api.open-meteo.com/v1/archive",
        params={
            "latitude": 59.33,
            "longitude": 18.07,
            "start_date": "2024-01-01",
            "end_date": "2026-10-23",
            "daily": "temperature_2m_mean,temperature_2m_min,temperature_2m_max,precipitation_sum",
            "timezone": "Europe/Stockholm",
        },
        timeout=10,
    )

    # kollar att datan vi får in stämmer överens med vad vi förväntar att få
    assert data is not None
    assert data["latitude"] == 59.33
    assert data["longitude"] == 18.07

    assert "latitude" in data  # kollar att viktiga "keys" finns med i json filen.
    assert "longitude" in data
    assert "daily" in data

    assert isinstance(
        data, dict
    )  # isinstance kollar om ett värde är just den här typen av data som specifieras i koden. I detta fall data == dict
    assert isinstance(data["latitude"], (int, float))
    assert isinstance(data["daily"]["temperature_2m_mean"], list)


def test_hamta_vaderdata():  # själva testet som testar funktionen hamta_vaderdata() och kollar att den returnerar data i rätt format. Detta test kommer att göra ett riktigt anrop till API:et.
    data = hamta_vaderdata()

    assert data is not None
    assert "latitude" in data
    assert "longitude" in data
    assert "daily" in data

    assert isinstance(data, dict)
    assert isinstance(data["latitude"], (int, float))
    assert isinstance(data["daily"]["temperature_2m_mean"], list)
