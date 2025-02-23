import requests
from datetime import datetime

USERNAME = "shivam2005"
TOKEN = "hsbg42th42jo42jtoj2knw3tj34"
GRAPH_ID = "graph001"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id" : GRAPH_ID,
    "name" : "Reading",
    "unit" : "pages",
    "type" : "int",
    "color" : "ajisai"
}
headers = {
    "X-USER-TOKEN" : TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : input("How many pages you read today ?"),
}
response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20250222"
update_data = {
    "quantity" : "2"
}
# response = requests.put(url=update_pixel_endpoint, json=update_data, headers=headers)
# print(response.text)

# response = requests.delete(url=update_pixel_endpoint, headers=headers)
# print(response.text)