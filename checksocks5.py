import requests

def check_proxy(proxy):
    try:
        url = "https://httpbin.org/ip"
        proxies = {"http": f"socks5://{proxy}", "https": f"socks5://{proxy}"}
        response = requests.get(url, proxies=proxies, timeout=5)
        if response.status_code == 200:
            print(f"Working proxy: {proxy}")
            return True
    except:
        pass
    return False

with open("socks5_proxies.txt") as f:
    proxies = f.read().splitlines()

working_proxies = [p for p in proxies if check_proxy(p)]

with open("working_socks5.txt", "w") as f:
    f.write("\n".join(working_proxies))

print(f"Valid proxies saved: {len(working_proxies)}")