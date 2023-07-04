import requests

# Fetches the csv from the given url
# Returns the name of the file where it is stored
# Currently always saved as data.csv 
def fetch(url : str) -> str:
    response = requests.get(url)
    assert response.status_code == 200, 'Wrong status code'

    data_file = 'data.csv'
    data = str(response.content)[2:-1]

    with open(data_file, 'w') as f:
        f.write(data)

    return data_file