
from dotenv import load_dotenv
from openai import OpenAI # type: ignore
import streamlit as st

load_dotenv()

client = OpenAI()

#title of the app
st.title("Dubai Trip Assistant App")

# Initial message in the app
initial_message = [{"role": "system","content": "your role is to plan the dubai trips accordingly. ask question to the user about their needs.Answer questions professionally and use 200 or below words to answer."},
{"role": "assistant","content": "Hello, I am Dubai Guide bot, your expert trip planner.How can i help you today?"}]

# if no message in app set initial message
if "messages" not in st.session_state:
    st.session_state.messages = initial_message

# Function 
def get_response_from_llm(messages):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    return completion.choices[0].message.content

# Display previous chat messages
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# taking input from user and displaying it
user_message = st.chat_input("Enter your message")
if user_message:
    new_message = {"role": "user","content": user_message}
    st.session_state.messages.append(new_message)
    with st.chat_message(new_message["role"]):
        st.markdown(new_message["content"])

# taking response from assistant and dispalying it
    response = get_response_from_llm(st.session_state.messages)
    if response:
        response_message = {"role": "assistant","content": response}
        st.session_state.messages.append(response_message)
        with st.chat_message(response_message["role"]):
            st.markdown(response_message["content"])
