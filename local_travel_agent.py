import os
import streamlit as st
from textwrap import dedent
from phi.assistant import Assistant
from ai71 import AI71 

# Set up the Streamlit app
st.title("AI Travel Planner ✈️")
st.caption("Plan your next adventure with AI Travel Planner. Research and plan a personalized itinerary using Falcon AI71.")

# Read Falcon AI71 API key from .env file (assuming it's named FALCON_API_KEY)
falcon_api_key = os.getenv("FALCON_API_KEY")

if falcon_api_key:
    # Create Falcon AI71 Assistant with API key from .env
    falcon_assistant = Assistant(
        name="Falcon Assistant",
        role="Researches destinations, activities, and creates itineraries based on user preferences",
        llm=A(api_key=falcon_api_key),
        description=dedent(
            """
            I am your AI travel companion powered by Falcon AI71. 
            Tell me where you want to go and how long you have, and I'll help you research 
            destinations, activities, and create a draft itinerary for your dream vacation.
            """
        ),
        instructions=[
            "Given a travel destination and the number of days the user wants to travel for, generate a list of relevant search terms for finding travel activities and accommodations.",
            "Use Falcon AI71's capabilities to research these terms and provide the user with a draft itinerary that includes suggested activities and accommodations.",
            "Ensure the itinerary is well-structured, informative, and engaging.",
            "Focus on clarity, coherence, and overall quality.",
        ],
    )

    # Input fields for user's destination and travel duration
    destination = st.text_input("Where do you want to go?")
    num_days = st.number_input("How many days do you want to travel for?", min_value=1, max_value=30, value=7)

    if st.button("Generate Itinerary"):
        with st.spinner("Processing..."):
            # Get the response from the assistant
            response = falcon_assistant.run(f"{destination} for {num_days} days", stream=False)
            st.write(response)
