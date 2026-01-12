import os, requests
HA_URL = "http://supervisor/core/api"
TOKEN = os.environ["SUPERVISOR_TOKEN"]
HEADERS = {"Authorization": f"Bearer {TOKEN}","Content-Type": "application/json"}

def call_service(entity, service, data):
    domain = entity.split(".")[0]
    requests.post(f"{HA_URL}/services/{domain}/{service}", headers=HEADERS,
                  json={"entity_id": entity, **data})

def get_entities():
    r = requests.get(f"{HA_URL}/states", headers=HEADERS)
    return [e["entity_id"] for e in r.json()]
