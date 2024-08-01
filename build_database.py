import json
from protocols import INTERFACES
from services import ALL_SERVICES

data = {
    "protocols": INTERFACES,
    "services": ALL_SERVICES
}

with open('database.json', 'w') as f:
    json.dump(data, f, default=vars, indent=4)