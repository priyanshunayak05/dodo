import requests
import os
import json

api_key = "AIzaSyApF3_yU0s-bzfL5Hv2O6Qk368wgH3cxI4"
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:streamGenerateContent?key={api_key}"

headers = {"Content-Type": "application/json"}
data = {"contents": [{"parts": [{"text": "Hello"}]}]}

print("Sending request...")
with requests.post(url, headers=headers, json=data, stream=True) as response:
    print("Status:", response.status_code)
    for line in response.iter_lines():
        if line:
            print("RAW:", line.decode('utf-8'))
