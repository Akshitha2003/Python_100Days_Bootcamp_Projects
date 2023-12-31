import requests
from datetime import datetime

USERNAME = "akshithamary"
TOKEN = "Akshi123"

# To create a new pixela user
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

headers = {
    "X-USER-TOKEN": TOKEN
}

# To create a new graph definition
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
# response = requests.post(url=graph_endpoint, json=graph_config,headers=headers)
# print(response.text)

# Post a pixel
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config["id"]}"
today = datetime.now()
pixel_creation_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometres did you cycle today? - ")
}
response = requests.post(url=pixel_creation_endpoint, json=pixel_creation_config, headers=headers)
print(response.text)

# Update a pixel
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config["id"]}/{pixel_creation_config["date"]}"
pixel_update_config = {
    "quantity": "15.75"
}
# response = requests.put(url=pixel_update_endpoint, json=pixel_update_config, headers=headers)
# print(response.text)

# Delete a pixel
pixel_delete_endpoint = pixel_update_endpoint
# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)
