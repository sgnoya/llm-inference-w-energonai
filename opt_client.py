# %%
# %%
import json

import requests
import streamlit as st


def chat_opt(prompt, top_k=20, top_p=0.6, temperature=0.7, max_tokens=256):
    url = "http://0.0.0.0:8020/generation"
    data = {
        "max_tokens": max_tokens,
        "prompt": prompt,
        "top_k": top_k,
        "top_p": top_p,
        "temperature": temperature,
    }
    headers = {"Content-Type": "application/json"}

    req = requests.post(url, data=json.dumps(data), headers=headers)
    return req.json()["text"].replace(prompt, "")


def main():
    prompt = st.text_area("chatinput", "Hello World!")
    response = chat_opt(prompt)
    st.text(response.replace(".", ".\n").replace("?", "?\n"))


if __name__ == "__main__":
    main()
