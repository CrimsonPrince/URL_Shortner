import requests

form_data = {"url": "http://arthurcoll.com"}

r = requests.post("http://127.0.0.1:5000/submit", data = form_data)
