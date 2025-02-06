import requests
import json
# cat-classifier
url = "http://a624aa2ba23b6401191076defbb145f6-1412609712.ap-south-1.elb.amazonaws.com/v1/models/imagenet-vit:predict"

with open("input.json") as f:
    payload = json.load(f)
headers = {"Host": "imagenet-vit.default.emlo.tsai", "Content-Type": "application/json"}

response = requests.request("POST", url, headers=headers, json=payload)

print(response.headers)
print(response.status_code)
print(response.json())