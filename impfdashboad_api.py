import requests

def download_data():
    url = "https://impfdashboard.de/static/data/germany_vaccinations_timeseries_v2.tsv"
    r = requests.get(url)
    with open("data.csv", "wb") as f:
        f.write(r.content)