from asyncio import events
import json
from threading import local
import requests

with open('data/food_trucks.json', encoding='utf-8') as f:
    items = json.loads(f.read())
    our_events = items['data']['events']
    locations = items['data']['locations']
    vendors = items['data']['vendors']

for event in our_events:
    r = requests.post('http://127.0.0.1:5000/event/new', json = event)
    if r.status_code == requests.codes.ok:
        print(f"Created event {event['name']} with ID {r.text}")

for locale in locations:
    r = requests.post('http://127.0.0.1:5000/location/new', json = locale)
    if r.status_code == requests.codes.ok:
        print(f"Created location {locale['name']} with ID {r.text}")

for vendor in vendors:
    if not vendor['cuisines'] or not vendor['events']:
        continue
    r = requests.post('http://127.0.0.1:5000/vendor/new', json = vendor)
    if r.status_code == requests.codes.ok:
        print(f"Created vendor {vendor['name']} with ID {r.text}")
