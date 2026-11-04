
# 🌤️ Väderapplikation – Flask

## Om projektet

Detta projekt är en webbaserad väderapplikation utvecklad med Python, Flask, Pandas och Plotly. Applikationen hämtar väderdata från ett externt väder-API (Open-meteo) och presenterar informationen med ett enkelt format som tabeller och diagram.

Syftet med projektet är att hämta, bearbeta och visualisera väderdata samt ge användaren möjlighet att filtrera och jämföra väderinformation för olika datum och tidsperioder.

## Funktioner

- Hämta väderdata från ett externt API.
- Visa väderinformation i webbläsaren.
- Presentera medeltemperatur och nederbörd.
- Filtrera väderdata baserat på ett specifikt datum.
- Jämföra väderdata mellan olika månader och tidsperioder.
- Visa väderdata i diagram med Plotly.
- Bearbeta och analysera data med Pandas.
- Hantera API-fel och saknad data.

## Tekniker

Projektet använder följande tekniker:

- **Python** : Programmeringsspråk.
- **Flask** : Webbramverk för att skapa webbapplikationen.
- **Jinja2** : Hantering av HTML-mallar.
- **Bootstrap** : Styling och responsiv design.
- **Pandas** : Bearbetning och analys av väderdata.
- **Plotly** : Visualisering av väderdata.
- **Requests** : Kommunikation med ett externt API.
- **Pytest** : Testning av applikationens funktioner.

## Installation

### 1. Klona projektet

```bash
git clone https://github.com/psyduckkills/Programmerin2_Grupp_Arbete.git
```

### 2. Skapa en venv för att begränsa programmet till en separat miljö som inte har kontakt med resten av din dator.

Windows:

```bash
python -m venv venv
```
MacOS och/eller Linux:

```bash
python3 -m venv venv
```

När din venv är skapad kan du aktivera miljön med denna kod:

Windows:

```bash
venv\Scripts\activate
```
MacOS och/eller Linux:

```bash
source .venv/bin/activate
```

### 3. Installera beroenden

```bash
pip install -r requirements.txt
```

### 4. Starta applikationen

```bash
flask run
```

Öppna sedan följande adress i webbläsaren:

```text
http://127.0.0.1:5000
```

## Testning

Projektet använder Pytest för att testa applikationens funktioner.

### Installera verktyg

```bash
pip install -r requirements-dev.txt
```

Kör samtliga tester med:

```bash
pytest --cov
```

## Vidareutveckling

Möjliga framtida förbättringar:

- Fler möjligheter att filtrera och jämföra väderdata.
- Fler typer av diagram och visualiseringar.
- Utökad felhantering vid API-anrop.
- Fler automatiserade tester.

## Författare

Utvecklat som ett Python- och Flask-projekt.
## källa

API:et hämtar väderdata för Stockholm från Open-Meteo Historical weather (https://open-meteo.com/en/docs/historical-weather-api) 

API data är licenserad under: CC BY 4.0