

import requests
from datetime import datetime

USERNAME = 'manav30'
TOKEN = 'kjvhdshfkjweh98f23y'
GRAPH_ID = 'graph'

pixdela_endpoint = 'https://pixe.la/v1/users'

user_params = {"token":TOKEN,
               "username":USERNAME,
               "agreeTermsOfService":"yes",
               "notMinor":"yes"
               }

# response = requests.post(url=pixdela_endpoint,json=user_params)
# print(response.text)

graps_endpoint = f'{pixdela_endpoint}/{USERNAME}/graphs'

graps_config = {
    'id': GRAPH_ID,
    'name': 'work',
    'unit': 'video',
    'type': 'int',
    'color': 'ajisai'
}

headers = {
    'X-USER-TOKEN' : TOKEN
}

# response = requests.post(url=graps_endpoint,json=graps_config,headers=headers)
# print(response.text)

pixel_creation_endpoint = f'{pixdela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

today = datetime.now()

pixel_data = {
    # 'date': '20230520',
    'date': today.strftime('%Y%m%d'),
    'quantity': '15'
}

responce = requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)
print(responce)


