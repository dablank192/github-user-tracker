import requests
import sys


def get_activity(username):
    url = f"https://api.github.com/users/{username}/events"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            shorter_data = []
            for event in data:
                event_info = {
                    "Event": event["type"],
                    "Repo": event["repo"]["name"],
                    "URL": event["repo"]["url"]
                }
                shorter_data.append(event_info)
            return shorter_data
        else:
            return f"Some error occur: {response.status_code}"
    except Exception as e:
        return f"Error: {e}"
    
def main():
    print("---USER ACTIVITIES TRACKING PROGRAM---")
    print("Enter 'exit' or 'quit' to escape ")

    while True:
        user_input = input("Enter Username: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Exitting...")
            sys.exit()
        
        if not user_input:
            continue

        print("Fetching...")
        result = get_activity(user_input)

        print(f"{user_input}'s Activities:\n")
        if result: 
            for i, event in enumerate(result, 1):
                print(f"{i}. Event: {event["Event"]}\n")
                print(f"\tRepo's Name: {event["Repo"]}\n")
                print(f"\tRepo's URL: {event["URL"]}\n")
                print("-"*20)

        else:
            print("No Activities Found!")

        print("="*30)

if __name__ == "__main__":
    main()
