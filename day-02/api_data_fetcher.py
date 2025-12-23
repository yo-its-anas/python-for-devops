import requests
import json
API_KEY =  "GET_YOUR_API_KEY"
url = f"https://jooble.org/api/{API_KEY}"

headers = {
    "Content-Type": "application/json"
}

role = input("Enter job role: ")
location = input("Enter job location: ")

payload = {
    "keywords": role,
    "location": location
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    data = response.json()

    with open("jobs_output.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("Data saved to jobs_output.json")

    print("Jobs found:", data.get("totalCount", 0))
    for job in data.get("jobs", [])[:3]:
        print("\nTitle:", job.get("title"))
        print("Company:", job.get("company"))
        print("Location:", job.get("location"))
        print("Link:", job.get("link"))
else:
    print("Error:", response.status_code, response.text)