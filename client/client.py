from urllib.request import urlopen
from urllib.error import HTTPError, URLError
 
url = "http://server:8080/"
 
try:
    response = urlopen(url)
    encodedContent = response.read()
    print(encodedContent.decode('utf-8'))
    response.close()
except HTTPError as e:
    print(f"!!!HTTP Error: {e.code}")
except URLError as e:
    print(f"!!!URL Error: {e.reason}")