import requests
import os
from requests.auth import HTTPBasicAuth

CLIENT_ID = os.environ['SONG_SKIPPER_CLIENT_ID']
CLIENT_SECRET = os.environ['SONG_SKIPPER_CLIENT_SECRET']
REDIRECT_URI = os.environ['SONG_SKIPPER_REDIRECT_URI']

scope = 'user-read-currently-playing'
refresh_token = os.environ['SONG_SKIPPER_REFRESH_TOKEN']

'''
Retrieved the auth code, let's hope this works now. This is required when we are first trying to retrieve the access token. From here on out, the refresh token 
can be used instead
response = requests.get('https://accounts.spotify.com/authorize',
                        params={
                            'client_id': CLIENT_ID,
                            'response_type': 'code',
                            'redirect_uri': REDIRECT_URI
                        })
print(response.content)
'''
'''
# Retrieving a token
response = requests.post('https://accounts.spotify.com/api/token',
                         data={
                             'grant_type': 'authorization_code',
                             'code': auth_code,
                             'redirect_uri': 'https://www.google.com/'
                         },
                         auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET),
                         headers={
                             'Content-Type': 'application/x-www-form-urlencoded'
                         },)

print(response.json())
'''


# This bit of code will now return the refresh tokens
response = requests.post('https://accounts.spotify.com/api/token',
                         data={
                             'grant_type': 'refresh_token',
                             'refresh_token': refresh_token
                         },
                         headers={'Content-Type': 'application/x-www-form-urlencoded'},
                         auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET))

access_token = response.json()['access_token']

current = requests.get('https://api.spotify.com/v1/me/player/currently-playing',
                        headers={
                            'Authorization': 'Bearer ' + access_token
                        })

print(current.json()['item']['name'])