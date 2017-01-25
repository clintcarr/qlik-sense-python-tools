import requests
from requests_ntlm import HttpNtlmAuth
requests.packages.urllib3.disable_warnings()

headers = {"X-Qlik-XrfKey": "abcdefg123456789",
            "Accept": "application/json",
            "X-Qlik-User": "UserDirectory=Internal;UserID=sa_repository",
            "Content-Type": "application/json",
            "Connection": "Keep-Alive"}

session = requests.Session()
session.auth = HttpNtlmAuth('qliklocal\\administrator','Qlik1234', session)
x = session.get('https://qs2.qliklocal.net/qrs/about?xrfkey=abcdefg123456789', verify=False, headers = headers)
url = x.url
y = session.get(url.replace('form', 'windows_authentication'), verify=False, headers = headers)

print (y.content)
