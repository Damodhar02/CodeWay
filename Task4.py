import requests

def get_weather(api_key, location):
    # OpenWeatherMap API URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

    # Send HTTP request to the API
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract relevant weather information
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        description = data['weather'][0]['description']

        # Display weather information
        print(f"Weather in {location}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Description: {description}")
    else:
        print("Error fetching weather data. Please try again later.")

def main():
    # API key from OpenWeatherMap (replace with your own API key)
    api_key = 'YOUR_API_KEY'

    # Prompt the user to enter the city name or zip code
    location = input("Enter the city name or zip code: ")

    # Get weather information
    get_weather(api_key, location)

if __name__ == "__main__":
    main()
