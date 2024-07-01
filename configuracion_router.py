import requests
import json

# Variables
url = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces/interface=Loopback11"
username = "cisco"
password = "cisco123!"
headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

interface_data = {
    "ietf-interfaces:interface": {
        "name": "Loopback11",
        "description": "VIDAL-LORCA",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "11.11.11.11",
                    "netmask": "255.255.255.255"
                }
            ]
        }
    }
}


response = requests.put(
    url,
    headers=headers,
    auth=(username, password),
    data=json.dumps(interface_data),
    verify=False  # Deshabilitar verificación SSL para propósitos de prueba
)

# Mostrar la respuesta
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
