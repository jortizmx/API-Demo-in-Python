import requests

API_URL = "https://api.github.com/repos/python/cpython"

def main():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()

        print("Repository:", data.get("name"))
        print("Stars:", data.get("stargazers_count"))
        print("Forks:", data.get("forks_count"))

    except Exception as e:
        print("Error calling API:", e)

if __name__ == "__main__":
    main()
