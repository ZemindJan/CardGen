import requests

response = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vQfcuVJtXMn4PGIY7id1qMlOi4IbkVqFpqSArPBe-YZlKZ2crQuPx_IzHGe5O8z86uPB93QAykHNT4T/pub?gid=1392430569&single=true&output=csv')
assert response.status_code == 200, 'Wrong status code'

data_file = 'data.csv'
data = str(response.content)[2:-1]

with open(data_file, 'w') as f:
    f.write(data)