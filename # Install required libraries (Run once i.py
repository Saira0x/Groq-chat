# Install required libraries (Run once in Colab)
!pip install -q groq gradio


import os
import gradio as gr
from groq import Groq


# Initialize Groq Client
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


# Chat function
def chat_with_groq(message, history):

    messages = []

    # Add previous conversation
    for user_msg, bot_msg in history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": bot_msg})

    # Add current message
    messages.append({"role": "user", "content": message})

    # Call Groq API
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama-3.3-70b-versatile",
    )

    response = chat_completion.choices[0].message.content

    return response


# Gradio Interface
demo = gr.ChatInterface(
    fn=chat_with_groq,
    title="Groq AI Chatbot",
    description="Simple AI Chatbot using Groq API + Gradio",
    theme="soft"
)


# Launch App
demo.launch(share=True)
