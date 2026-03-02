import sys
import urllib.request

def check_url(url):
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            print(f"URL: {url}")
            print(f"Status Code: {response.getcode()}")
            print("Status: Reachable")
    except Exception as e:
        print(f"URL: {url}")
        print(f"Error: {e}")
        print("Status: Unreachable")

if __name__ == "__main__":
    target_url = sys.argv[1] if len(sys.argv) > 1 else "https://www.google.com"
    check_url(target_url)
