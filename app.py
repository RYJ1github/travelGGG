import streamlit as st
import openai
import requests
import logging

# Define your API keys here
OPENAI_API_KEY = 'your_openai_api_key_here'
TRIPADVISOR_API_KEY = 'your_tripadvisor_api_key_here'

# Initialize OpenAI
openai.api_key = OPENAI_API_KEY

# Streamlit Title
st.title("Travel GPT - AI Agent for Travel Destination Queries")

# Disable logger propagation
logging.getLogger("python_utils.logger").propagate = False

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Function to fetch travel information from TripAdvisor API
def get_tripadvisor_info(query):
    url = f"https://api.tripadvisor.com/api/v2.0/locations/search?query={query}&key={TRIPADVISOR_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve data from TripAdvisor"}

# Function to process and summarize information using OpenAI
def get_openai_summary(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# React to user input
if prompt := st.chat_input("I am a helpful travel bot. Ask me anything about travel destinations!"):
    try:
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Process the user input
        with st.chat_message("assistant"):
            st.markdown("Let me check that for you...")

        # Fetch information from TripAdvisor
        travel_info = get_tripadvisor_info(prompt)
        
        if "error" in travel_info:
            raise Exception(travel_info["error"])

        # Generate summary using OpenAI
        summary = get_openai_summary(f"Summarize the following travel information: {travel_info}")

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(summary)
        st.session_state.messages.append({"role": "assistant", "content": summary})

    except Exception as e:
        logging.error(f"Error: {e}")
        if 'insufficient_quota' in str(e):
            message = "I was not able to process the request because the API quota has been exceeded. Please check back later or contact support for assistance."
        else:
            message = f"I was not able to process the request. Error: {e}"
        with st.chat_message("assistant"):
            st.markdown(message)
        st.session_state.messages.append({"role": "assistant", "content": message})
