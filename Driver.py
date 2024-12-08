import os
from dotenv import load_dotenv, find_dotenv
import streamlit as st
from Crew import create_convo

# Gen environment variables from file
_ = load_dotenv(find_dotenv())


# Set the title using StreamLit
st.title(' Conversation Generator ')

input_char1 = st.text_input('Enter the first character in the Conversation')
input_char2 = st.text_input('Enter the second character in the Conversation')
input_topic = st.text_input('What topic are they talking about?')

if st.button("Generate Converstaion"):
    conversation = create_convo(input_char1, input_char2, input_topic)

    st.write(conversation) 