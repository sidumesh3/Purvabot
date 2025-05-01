
import streamlit as st
import openai

import os
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load the knowledge base
with open("purva_industries_faq.txt", "r", encoding="utf-8") as file:
    purva_data = file.read()

# Streamlit UI
st.title("Purva Industries Virtual Helpdesk")
st.markdown("Instant answers about pricing, logistics, product info, and company background.")

user_question = st.text_input("Your Question")

if user_question:
    system_prompt = f"""You are a helpful assistant for a company called Purva Industries. 
Use only the following context to answer the user's question:

{purva_data}"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_question}
        ],
        temperature=0.2
    )

    st.write("**PurvaBot:**", response.choices[0].message.content)
