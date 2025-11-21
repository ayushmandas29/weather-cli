import requests

def get_weather(city):
    url=f"https://wttr.in/{city}?format=3"
    try:
        r=requests.get(url, timeout=5)
        print("\nWeather Report:")
        print(r.text)
    except Exception:
        print("Error fetching weather. Check connection.")

def main():
    print("=== Advanced Weather App (CLI) ===")
    city=input("Enter city name: ").strip()
    if city:
        get_weather(city)
    else:
        print("No city entered.")

if __name__=="__main__":
    main()
