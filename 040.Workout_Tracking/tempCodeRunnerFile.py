response = requests.post(url=URL, json=parameters, headers=headers)
print(response.json())