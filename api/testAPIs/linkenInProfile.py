import http.client

API_KEY = 'ed9d133ce5msheed192e1aaa3916p1e1ec4jsn6f2154264862'
conn = http.client.HTTPSConnection("linkedin-profiles1.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': API_KEY,
    'X-RapidAPI-Host': "linkedin-profiles1.p.rapidapi.com"
}

conn.request("GET", "/search?query=Excel&type=person", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))