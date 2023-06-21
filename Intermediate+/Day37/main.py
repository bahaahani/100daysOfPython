import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":"MEOWMEOWMEOWMEOWMEOWMEOWMEOWMEOWMEOWMEOWMEOWMEOWMEOWMEOWMEOW",
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
    "timezone":"Bahrain/Manama"
}