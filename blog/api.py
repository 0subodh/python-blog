import requests
username = 'subodh1adhikari121'
token = '9f8c4f9e109b6ee7d4d0daef03ce17cc78ad6f0a'

response = requests.get(
    'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(
        username=username
    ),
    headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
    print('CPU quota info:')
    print(response.content)
else:
    print('Got unexpected status code {}: {!r}'.format(
        response.status_code, response.content))
