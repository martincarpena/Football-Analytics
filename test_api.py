import os
from dotenv import load_dotenv
import requests

load_dotenv()
api_key = os.getenv("API_FOOTBALL_KEY")

url = "https://v3.football.api-sports.io/fixtures"
headers = {"x-apisports-key": api_key}
params = {"league": 71, "season": 2024}

response = requests.get(url, headers=headers, params=params)
data = response.json()

print("Total matches found:", data["results"])
print()
print("Errors:", data["errors"])
print()
print("Full response:", data)