import streamlit as st
import google as genai

# Configure API key
api_key = "AIzaSyB7sXwTv82pOethlPFUqSO0yPakQtUzCxE"
genai.configure(api_key=api_key)

# Generation settings
generation_config = {
    "temperature": 0.4,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 2048,
}

# Initialize model
model = genai.GenerativeModel(
    model_name="gemini-pro",
    generation_config=generation_config,
)

# ===============================
# FUNCTION (MOVE HERE)
# ===============================
def generate_itinerary(destination, days, nights):

    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    f"Write me a travel itinerary to {destination} for {days} days and {nights} nights."
                ],
            }
        ]
    )

    response = chat_session.send_message(
        f"Create a detailed travel itinerary for {days} days and {nights} nights in {destination}."
    )

    return response.text


#
# ===============================

st.set_page_config(page_title="TravelGuideAI", page_icon="🌍", layout="centered")

st.title("🌍 Explore with AI: Custom Itineraries for Your Next Journey")

st.markdown("""
TravelGuideAI generates personalized travel plans based on your destination,
trip duration, and preferences — making travel planning simple and efficient.
""")

st.divider()

# Inputs
destination = st.text_input("📍 Enter your destination")

days = st.number_input(
    "📅 Enter number of days",
    min_value=1,
    step=1
)

nights = st.number_input(
    "🌙 Enter number of nights",
    min_value=0,
    step=1
)

st.divider()

# Generate button
if st.button("✨ Generate Personalized Itinerary"):

    if destination.strip() == "":
        st.warning("Please enter a destination.")
    else:
        with st.spinner("Generating your AI travel plan..."):

            result = generate_itinerary(destination, days, nights)

            st.success("Your itinerary is ready!")

            st.subheader("📖 Generated Itinerary")

            st.markdown(result)

