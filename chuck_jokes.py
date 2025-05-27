import requests

def get_joke():
    url = "https://api.chucknorris.io/jokes/random"
    try:
        response = requests.get(url)
        response.raise_for_status() # Raise error for bad status codes
        data = response.json()
        return data["value"]
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
    
def main():
    while True:
        print("\n--- Chuck Norris Jokes ---")
        print("1. Get a joke")
        print("2. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            print(f"\n🤣 {get_joke()}")
        elif choice == "2":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()