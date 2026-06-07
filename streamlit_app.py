import streamlit as st
import datetime
import webbrowser

st.set_page_config(page_title="Trivya AI ", page_icon="🎤")

st.title("🎤 Trivya AI ")
st.write("Type a command and see how the assistant responds.")

if "chat" not in st.session_state:
    st.session_state.chat = []


def process_command(command):
    command = command.lower()

    if "hello" in command:
        return "Hello, ask me anything! I can tell you the time, date, or even a joke!"

    elif "time" in command:
        return datetime.datetime.now().strftime("%I:%M %p")

    elif "date" in command:
        return datetime.datetime.now().strftime("%d %B %Y")

    elif "how are you" in command:
        return "I am doing well, thank you for asking!"

    elif "what is your name" in command:
        return "My name is Trivya, your voice assistant"

    elif "joke" in command:
        return "Why don't scientists trust atoms? Because they make up everything!"

    elif "youtube" in command:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    elif "google" in command:
        webbrowser.open("https://google.com")
        return "Opening Google"

    elif "github" in command:
        webbrowser.open("https://github.com")
        return "Opening GitHub"

    elif "exit" in command:
        return "Goodbye!"

    else:
        return "Sorry, I didn't understand that command."


user_input = st.text_input("Ask trivya anything... ")

if st.button("Ask"):
    if user_input:
        response = process_command(user_input)

        st.session_state.chat.append(("You", user_input))
        st.session_state.chat.append(("Bot", response))

for sender, msg in st.session_state.chat:
    if sender == "You":
        st.markdown(f"**You:** {msg}")
    else:
        st.markdown(f"**Bot:** {msg}")