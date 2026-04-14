import requests
import os

MANUS_API_KEY = os.environ.get("MANUS_API_KEY")

PROMPT = """
Найди деловые мероприятия с топ-менеджерами (CEO, CFO, HRD) в России.
Только очные мероприятия. Сохрани результат в виде списка.
"""

url = "https://api.manus.ai/v1/tasks"

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "API_KEY": MANUS_API_KEY
}

data = {
    "prompt": PROMPT,
    "mode": "fast"
}

response = requests.post(url, json=data, headers=headers)

print(response.json())
