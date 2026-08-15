import json
import urllib.parse
import urllib.request

query = input("Enter the types of news: ").strip()

if not query:
    print("Please enter a valid news type.")
    raise SystemExit(1)

api_key = "pub_729f61bdca274b4397b979599b16cccc"
params = urllib.parse.urlencode({"apikey": api_key, "q": query})
url = f"https://newsdata.io/api/1/news?{params}"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode("utf-8"))

print(f"News type: {query}")
for article in data.get("results", []):
    print(article.get("title", "No title"))
