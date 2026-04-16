import random
import datetime

# ---- Tool: Get Weather (Mock Real-Time) ----
def get_weather(city):
    weather_data = [
        {"temp": 35, "condition": "Sunny ☀️", "humidity": 55, "wind": 12},
        {"temp": 28, "condition": "Cloudy ☁️", "humidity": 65, "wind": 8},
        {"temp": 24, "condition": "Rainy 🌧️", "humidity": 85, "wind": 15},
        {"temp": 18, "condition": "Cool 🌥️", "humidity": 70, "wind": 10}
    ]

    data = random.choice(weather_data)
    data["city"] = city
    data["time"] = datetime.datetime.now().strftime("%H:%M:%S")
    return data


# ---- Outfit Logic ----
def suggest_outfit(temp, condition, preference, occasion, sensitivity):
    suggestion = ""

    # Weather based suggestion
    if "Rainy" in condition:
        suggestion += "Carry an umbrella ☔. "

    if temp > 32:
        suggestion += "Wear light cotton clothes. "
    elif temp > 25:
        suggestion += "Comfortable casual wear is fine. "
    else:
        suggestion += "Wear a jacket or sweater. "

    # Preference based suggestion
    if preference.lower() == "formal":
        suggestion += "Choose formal shirt and trousers. "
    elif preference.lower() == "sporty":
        suggestion += "Choose breathable sportswear. "
    else:
        suggestion += "Choose casual comfortable outfit. "

    # Occasion based suggestion
    if occasion.lower() == "office":
        suggestion += "Office-appropriate attire is recommended. "
    elif occasion.lower() == "party":
        suggestion += "Stylish trendy wear is recommended. "
    elif occasion.lower() == "gym":
        suggestion += "Flexible activewear is recommended. "

    # Sensitivity based suggestion
    if sensitivity.lower() == "hot":
        suggestion += "Use lighter layers because you feel hot easily."
    elif sensitivity.lower() == "cold":
        suggestion += "Wear extra layers because you feel cold easily."
    else:
        suggestion += "Standard layering is enough."

    return suggestion


# ---- ReAct Agent ----
class WeatherAgent:

    def run(self, city, preference, occasion, sensitivity):
        print("\n" + "="*70)
        print(f"User Input: city={city}, preference={preference}, occasion={occasion}, sensitivity={sensitivity}")

        # Thought 1
        print("\n🧠 Thought 1: I need to retrieve weather data for the city.")
        print("⚙️ Action 1: Calling get_weather tool...")

        weather = get_weather(city)

        print(f"👀 Observation 1: Temp={weather['temp']}°C, Condition={weather['condition']}")

        # Thought 2
        print("\n🧠 Thought 2: I need to check the user's outfit preference.")
        print(f"👀 Observation 2: User prefers {preference} style.")

        # Thought 3
        print("\n🧠 Thought 3: I need to consider the occasion.")
        print(f"👀 Observation 3: The user is dressing for {occasion}.")

        # Thought 4
        print("\n🧠 Thought 4: I need to adjust recommendation based on temperature sensitivity.")
        print(f"👀 Observation 4: User has {sensitivity} temperature sensitivity.")

        # Action Final
        print("\n⚙️ Action 2: Generating personalized outfit suggestion...")

        outfit = suggest_outfit(weather["temp"], weather["condition"], preference, occasion, sensitivity)

        # Final Answer
        print("\n✅ Final Answer:")
        print(f"📍 City: {weather['city']}")
        print(f"⏰ Time: {weather['time']}")
        print(f"🌡️ Temperature: {weather['temp']}°C")
        print(f"🌤️ Condition: {weather['condition']}")
        print(f"👗 Outfit Suggestion: {outfit}")


# ---- Run ----
agent = WeatherAgent()

city = input("Enter City: ")
preference = input("Enter Outfit Preference (casual/formal/sporty): ")
occasion = input("Enter Occasion (office/party/gym): ")
sensitivity = input("Temperature Sensitivity (hot/normal/cold): ")

agent.run(city, preference, occasion, sensitivity)
