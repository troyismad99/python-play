import requests

# http://api.open-notify.org/astros.json
# {
#   "message": "success",
#   "number": NUMBER_OF_PEOPLE_IN_SPACE,
#   "people": [
#     {"name": NAME, "craft": SPACECRAFT_NAME},
#     ...
#   ]
# }

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()
print(json)

print('The people currently in space are:')
for person in json['people']:
    print(person['name'])
