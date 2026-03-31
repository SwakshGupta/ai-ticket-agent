import streamlit as st
from agent.agent import run_agent

st.title("AI Ticket Agent")

query = st.text_input("Enter your issue:")

if st.button("Submit"):
    response = run_agent(query)
    st.write(response)