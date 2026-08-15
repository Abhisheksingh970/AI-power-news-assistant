import json
import urllib.parse
import urllib.request

query = input("Enter the types of news: ").strip()

if not query:
    print("Please enter a valid news type.")
    raise SystemExit(1)

api_key = "pub_729f61bdca274b4397b979599b16cccc"
params = urllib.parse.urlencode({"apikey": api_key, "q": query, "language": "en"})
url = f"https://newsdata.io/api/1/news?{params}"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode("utf-8"))

print(f"News type: {query}")
articles = data.get("results", [])[:10]  # Get first 10 articles

for i, article in enumerate(articles, start=1):
    title = article.get("title", "No title")
    description = article.get("description", "No description")
    print(f"\n{i}. Title: {title}")
    print(f"   Description: {description}")
