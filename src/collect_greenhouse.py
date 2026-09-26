import requests
from pathlib import Path

url = "https://boards-api.greenhouse.io/v1/boards/mongodb/jobs?content=true"

response = requests.get(url, timeout=15)
response.raise_for_status()
data = response.json()

print(type(data))
print(data.keys())
print(len(data['jobs']))

output_file = Path("data/private/jobs/mongodb_raw.json")
output_file.parent.mkdir(exist_ok=True, parents=True)
output_file.write_bytes(response.content)

print(f"Saved {output_file} ({output_file.stat().st_size} bytes)")