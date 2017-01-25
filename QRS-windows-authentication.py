import requests
from requests_ntlm import HttpNtlmAuth
requests.packages.urllib3.disable_warnings()

headers = {"X-Qlik-XrfKey": "abcdefg123456789",
            "Accept": "application/json",
            "X-Qlik-User": "UserDirectory=Internal;UserID=sa_repository",
            "Content-Type": "application/json",
            "Connection": "Keep-Alive"}

#establish a session (NTLM challenges on each request, performing all queries in a session prevents this)
session = requests.Session()
#set the session authentication to HttpNtlmAuth, attach it to the session
session.auth = HttpNtlmAuth('qliklocal\\administrator','Qlik1234', session)
#connect to the API qrs/about using Windows Authentication in the session
x = session.get('https://qs2.qliklocal.net/qrs/about?xrfkey=abcdefg123456789', verify=False, headers = headers)
#return the URL (this is the redirect from Qlik Sense https://qs2.qliklocal.net/form/?targetid{}
url = x.url
#replace the page form with windows_authentication and hit the url again
y = session.get(url.replace('form', 'windows_authentication'), verify=False, headers = headers)

print (y.content)
