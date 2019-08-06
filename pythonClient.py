__author__ = 'bdm4'

import requests, json

token_url = "https://dev-oauth.hydrofarm.com/connect/token"

test_api_url = "https://dev-api.hydrofarm.com/api/invoices/getinvoices"

#client (application) credentials on apim.byu.edu
client_id = '4839-3799-8b021592-aef2-4bfe-9143-1db17f000e9b'
client_secret = '4ISnBFVSL5a6gmgHeBWeKwwr0N/H79T6P4blouH5wrw='

#step A, B - single call with client credentials as the basic auth header - will return access_token
data = {'grant_type': 'client_credentials'}

access_token_response = requests.post(token_url, data=data, verify=False, allow_redirects=False, auth=(client_id, client_secret))

print access_token_response.headers
print access_token_response.text

tokens = json.loads(access_token_response.text)

print "access token: " + tokens['access_token']

#step B - with the returned access_token we can make as many calls as we want

api_call_headers = {'Authorization': 'Bearer ' + tokens['access_token']}
api_call_response = requests.get(test_api_url, headers=api_call_headers, verify=False)

print api_call_response.text