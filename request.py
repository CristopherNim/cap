import requests

url = 'http://localhost:5000/results'
r = requests.post(url, json={'bruise': 0, 'gill-attachment': 1, 'gill-spacing': 0, 'gill-size': 1, 'stalk-shape': 0})

print(r.json())