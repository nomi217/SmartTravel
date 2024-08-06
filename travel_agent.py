import requests
import streamlit as st
from textwrap import dedent

# Set up the Streamlit app
st.title("AI Travel Planner ✈️")
st.caption("Plan your next adventure with AI Travel Planner by researching and planning a personalized itinerary on autopilot using AI71.")

# Get AI71 API key from user
ai71_api_key = st.text_input("Enter AI71 API Key to access AI71", type="password")

# Get SerpAPI key from the user
serp_api_key = st.text_input("Enter Serp API Key for Search functionality", type="password")

# Base URL for AI71 API
ai71_base_url = "https://api.ai71.com"  # Replace with the actual base URL if different

def ai71_request(endpoint, data):
    headers = {
        'Authorization': f'Bearer {ai71_api_key}',
        'Content-Type': 'application/json'
    }
    response = requests.post(f"{ai71_base_url}/{endpoint}", json=data, headers=headers)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

if ai71_api_key and serp_api_key:
    # Function to simulate researcher assistant
    def researcher_assistant(destination, num_days):
        search_terms = [
            f"top activities in {destination} for {num_days} days",
            f"best accommodations in {destination} for {num_days} days",
            f"popular travel spots in {destination} for {num_days} days"
        ]
        
        results = []
        for term in search_terms:
            search_results = ai71_request("search", {"query": term})
            results.extend(search_results.get("results", []))
        
        return results[:10]  # Return top 10 results

    # Function to simulate planner assistant
    def planner_assistant(destination, num_days, research_results):
        data = {
            "destination": destination,
            "num_days": num_days,
            "research_results": research_results
        }
        response = ai71_request("generate_itinerary", data)
        return response.get("itinerary", "No itinerary generated.")

    # Input fields for the user's destination and the number of days they want to travel for
    destination = st.text_input("Where do you want to go?")
    num_days = st.number_input("How many days do you want to travel for?", min_value=1, max_value=30, value=7)

    if st.button("Generate Itinerary"):
        with st.spinner("Processing..."):
            # Simulate the research and planning process
            research_results = researcher_assistant(destination, num_days)
            itinerary = planner_assistant(destination, num_days, research_results)
            st.write(itinerary)
