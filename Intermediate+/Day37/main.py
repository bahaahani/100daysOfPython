import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "MEOWMEOWMEOWMEOWMEOWMEOWMEOWMEOWMEOWMEOWMEOWMEOWMEOWMEOWMEOW"
user_params = {
    "token":TOKEN,
    "username":"meowmeowmeow",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response =requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/meowmeowmeow/graphs"

graph_config = {
    "id":"graph1",
    "name":"Coding Graph",
    "unit":"hours",
    "type":"float",
    "color":"ajisai",
}

headers = {
    "X-USER-TOKEN":TOKEN,
}


# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/meowmeowmeow/graphs/graph1"
datetime_now = datetime.now()
date = datetime_now.strftime("%Y%m%d")
pixel_data = {
    "date": date,
    "quantity":"1",
}
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# response = requests.put(url=f"{pixel_creation_endpoint}/{date}", json={"quantity":"2"}, headers=headers)
# print(response.text)

response = requests.delete(url=f"{pixel_creation_endpoint}/{date}", headers=headers)
print(response.text)