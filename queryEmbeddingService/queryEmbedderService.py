import requests

url = "https://shaanSidd-embedder.hf.space/embed"

data = {
    "text": "2 bhk in lakhimpur kheri"
}

response = requests.post(url, json=data)

print(response.json())