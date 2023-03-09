#przyklad działania:
#pageurl – pobrana strona, date-data w formacie rok miesiac dzien np. 20230126
#zapytanie do api:
#http://archive.org/wayback/available?url=example.com&timestamp=20060101
import webbrowser

import requests as requests
pageurl = "demotywatory.pl"
url = "http://archive.org/wayback/available?url="+pageurl+"&timestamp="+str(20230126)
response = requests.get(url)
d = response.json()
page = d["archived_snapshots"]["closest"]["url"]
webbrowser.open(page)

url = "http://archive.org/wayback/available?url="+pageurl+"&timestamp="+str(20150126)
response = requests.get(url)
d = response.json()
page = d["archived_snapshots"]["closest"]["url"]
webbrowser.open(page)

url = "http://archive.org/wayback/available?url="+pageurl+"&timestamp="+str(20050126)
response = requests.get(url)
d = response.json()
page = d["archived_snapshots"]["closest"]["url"]
webbrowser.open(page)

