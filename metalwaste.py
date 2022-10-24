import json

def metalCollectors():
    value = {
        "collectors" : [
            {
                "name": "wa metal collectors",
                "address" : "no 26 borupana road ratmalana",
                "telephone":"011 2724561",
                "mail":"wa@gmail.com"
            },
            {
                "name": "ag metal collectors",
                "address": "no 54 galle road wellawatha",
                "telephone": "011 2454561",
                "mail": "ag@gmail.com"
            },
    ]
    }
    return json.dumps(value)

print(metalCollectors())