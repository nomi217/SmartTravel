# 🛫 AI Travel Agent
This Streamlit app is an AI-powered travel Agent that generates personalized travel itineraries using AI71. It automates the process of researching, planning, and organizing your dream vacation, allowing you to explore exciting destinations with ease.

## Features
Research and discover exciting travel destinations, activities, and accommodations
Customize your itinerary based on the number of days you want to travel
Utilize the power of GPT-4o to generate intelligent and personalized travel plans

## How to get Started?
Clone the GitHub repository

```
https://github.com/nomi217/SmartTravel.git
```
Install the required dependencies:
```
pip install -r requirements.txt
```
Get your AI71 API Key
Get your SerpAPI Key
Sign up for an SerpAPI account and obtain your API key.
Run the Streamlit App</br>
```
streamlit run travel_agent.py
```

## How it Works?
The AI Travel Agent has two main components:

- Researcher: Responsible for generating search terms based on the user's destination and travel duration, and searching the web for relevant activities and accommodations using SerpAPI.
- Planner: Takes the research results and user preferences to generate a personalized draft itinerary that includes suggested activity.
