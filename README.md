# thinkpalm-agentai-Kiruthiga-Lab2

# Weather Outfit Recommendation ReAct Agent

## Project Overview

This project is a **Weather Outfit Recommendation Agent** built in Python using the **ReAct (Reasoning + Acting)** framework.

The agent:

1. Retrieves weather data for a given city
2. Analyzes user outfit preferences
3. Considers the occasion
4. Adjusts recommendations based on temperature sensitivity
5. Generates a personalized outfit suggestion

This demonstrates how an AI agent can **reason step-by-step**, gather observations, and provide an intelligent recommendation.

---

## Features

* Mock real-time weather data generation
* Multi-step reasoning process using ReAct
* Personalized outfit recommendations based on:

  * Weather conditions
  * Outfit preference
  * Occasion
  * Temperature sensitivity
* Clear reasoning trace:

  * Thought
  * Action
  * Observation
  * Final Answer

---

## Inputs Required

The user provides the following inputs:

1. **City**

   * Example: `Chennai`

2. **Outfit Preference**

   * Options:

     * `casual`
     * `formal`
     * `sporty`

3. **Occasion**

   * Options:

     * `office`
     * `party`
     * `gym`

4. **Temperature Sensitivity**

   * Options:

     * `hot`
     * `normal`
     * `cold`

---

## ReAct Workflow

### Step 1: Retrieve Weather Data

The agent retrieves:

* Temperature
* Weather condition
* Humidity
* Wind speed

### Step 2: Analyze Outfit Preference

The agent checks the user's preferred clothing style.

### Step 3: Analyze Occasion

The agent considers the occasion such as office, party, or gym.

### Step 4: Analyze Temperature Sensitivity

The agent adjusts recommendations depending on whether the user feels hot or cold easily.

### Step 5: Generate Final Recommendation

The agent combines all observations and generates a personalized outfit recommendation.

---

## Technologies Used

* **Python**
* **Random Module**
* **Datetime Module**
* **ReAct Framework**

---

## Project Structure

```bash
weather_agent/
│── weather_agent.py
│── README.md
```

---

## How to Run

### Step 1: Clone or Download the Project

Save the Python file as:

```bash
weather_agent.py
```

### Step 2: Run the Program

```bash
python weather_agent.py
```

---

## Example Run

```bash
Enter City: Chennai
Enter Outfit Preference (casual/formal/sporty): formal
Enter Occasion (office/party/gym): office
Temperature Sensitivity (hot/normal/cold): hot
```

### Sample Output

```bash
🧠 Thought 1: I need to retrieve weather data for the city.
⚙️ Action 1: Calling get_weather tool...
👀 Observation 1: Temp=35°C, Condition=Sunny ☀️

🧠 Thought 2: I need to check the user's outfit preference.
👀 Observation 2: User prefers formal style.

🧠 Thought 3: I need to consider the occasion.
👀 Observation 3: The user is dressing for office.

🧠 Thought 4: I need to adjust recommendation based on temperature sensitivity.
👀 Observation 4: User has hot temperature sensitivity.

⚙️ Action 2: Generating personalized outfit suggestion...

✅ Final Answer:
📍 City: Chennai
👗 Outfit Suggestion: Wear light cotton clothes. Choose formal shirt and trousers. Office-appropriate attire is recommended. Use lighter layers because you feel hot easily.
```

---

## Learning Outcomes

This project demonstrates:

* AI reasoning with the ReAct pattern
* Tool usage simulation
* Context-aware recommendations
* Personalized AI responses
* Multi-step reasoning workflow

---

## Future Enhancements

Possible improvements:

1. Integrate real weather APIs
2. Add memory for previous user preferences
3. Add wardrobe recommendations by season
4. Add weather alerts
5. Build a web interface using Flask or Streamlit

---

## Author

Developed as part of **Lab 2 - ReAct Agent Enhancement Project**
