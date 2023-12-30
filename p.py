import requests

print(requests.post(url = 'http://127.0.0.1:8000/reaction/create_reaction/', json={
  "user_id": 1,
  "object_pk": 2,
  "content_type": "stridfsgng",
  "reac": "stsgsring",
}).text)