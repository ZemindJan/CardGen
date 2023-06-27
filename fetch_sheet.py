import requests
from links import CSV_LINKS
from settings import Settings

response = requests.get(
    CSV_LINKS[Settings.version])
assert response.status_code == 200, 'Wrong status code'

data_file = 'data.csv'
data = str(response.content)[2:-1]

with open(data_file, 'w') as f:
    f.write(data)
