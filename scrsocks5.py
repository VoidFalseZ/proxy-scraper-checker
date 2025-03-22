import requests
from bs4 import BeautifulSoup

url = "https://www.socks-proxy.net/"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

proxies = []
for row in soup.select("table tbody tr"):
    columns = row.find_all("td")
    ip = columns[0].text
    port = columns[1].text
    proxies.append(f"{ip}:{port}")

# Save to a file
with open("socks5_proxies.txt", "w") as f:
    f.write("\n".join(proxies))

print(f"Scraped {len(proxies)} proxies.")
