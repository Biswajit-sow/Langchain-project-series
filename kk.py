from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import SequentialChain
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()


if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False 


def toggle_dark_mode():
    st.session_state.dark_mode = not st.session_state.dark_mode


if st.session_state.dark_mode:
    background_color = "#06091C"
    text_color = "#FFFFFF"
    header_color = "#64B5F6"
    input_background = "#374151"
    button_color = "#90CAF9"
    sidebar_background = "#343A40"
    generated_text_bg = "#4B5563"
    label_color = "#81D4FA" 
    sidebar_text_color = "#FFFFFF"  
else:  
    background_color = "#E5DCE5"
    text_color = "#2E4053"
    header_color = "#1A5276"
    input_background = "#FFFFFF"
    button_color = "#3498DB"
    sidebar_background = "#EAF2F8"
    generated_text_bg = "#e5f5ff"
    label_color = "#0B3861"  # Dark Blue for labels in light mode
    sidebar_text_color = "#000000"  # Black for sidebar text in light mode

# --- CSS Styling ---
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {background_color};
        color: {text_color};
        font-family: 'Arial', sans-serif;
    }}
    h1 {{
        color: {header_color};
        text-align: center;
        padding-bottom: 20px;
        border-bottom: 2px solid #D0D3D4;
    }}
    h2 {{
        color: {header_color};
    }}
    .stTextInput > label, .stTextArea > label {{
        color: {label_color};
        font-weight: 1200; /* Make it Extra Bold */
        font-size: 18px; /* Even Bigger */
        text-shadow: 1px 1px 0 #A9CCE3; /* Add a subtle text shadow for extra pop */
    }}
    .stTextInput > div > div > input, .stTextArea > div > div > textarea {{
        background-color: {input_background};
        border: 1px solid #A9CCE3;
        border-radius: 6px;
        color: {text_color};
        padding: 8px;
    }}
    .stButton > button {{
        color: {text_color};
        background-color: {button_color};
        border: none;
        padding: 12px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        font-weight: bold;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }}
    .stButton > button:hover {{
        background-color: {header_color};
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }}
    .stSidebar {{
        background-color: {sidebar_background};
        padding: 20px;
        border-right: 2px solid #85C1E9;
        color: {sidebar_text_color}; /* Dynamic sidebar text color */
        font-size: 14px;
    }}
    .stSidebar h3 {{
        color: {header_color};
    }}
    .stSidebar > div > ul {{
        list-style-type: none;
        padding: 0;
    }}
    .stSidebar > div > ul > li {{
        margin-bottom: 10px;
    }}
    .stAlert {{
        background-color: #FFDCDC;
        color: #C0392B;
        padding: 12px;
        border-radius: 6px;
        margin-bottom: 10px;
    }}
    .stSuccess {{
        background-color: #D4EFDF;
        color: #1E8449;
        padding: 12px;
        border-radius: 6px;
        margin-bottom: 10px;
    }}
    /* Style for generated text */
    .generated-text {{
        padding: 12px;
        margin-bottom: 10px;
        border-left: 5px solid #3498db;
        background-color: {generated_text_bg};
        border-radius: 6px;
        color: {text_color};
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title('AI-Powered Product & Social Marketing Content Generator')

st.button("Toggle Dark Mode", on_click=toggle_dark_mode)

product_name = st.text_input("Product Name:", "Enter your product name")
features = st.text_area("Product Features (comma-separated):", "can you explain your product features")
keyword = st.text_input("SEO Keyword/Tone Modifier:", "give a keyword")

model_name = "tinyllama"
llm = Ollama(model=model_name)
output_parser = StrOutputParser()

title_prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a creative marketing expert. Generate a catchy product title. The title MUST be 5 words or less. Be very strict with this word limit!"),
    ("user", "Product Name: {product_name}\nFeatures: {features}\nCreative Title:")
])
title_chain = title_prompt_template | llm | output_parser

description_prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a marketing copywriter. Create a compelling product description. The description MUST be 5 sentences or less. Prioritize conciseness!"),
    ("user", "Product Title: {title}\nFeatures: {features}\nMarketing Description:")
])
description_chain = description_prompt_template | llm | output_parser

social_media_prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a social media manager. Create a concise social media caption (max 2 sentences), including the keyword. Do NOT exceed the sentence limit. Be direct."),
    ("user", "Product Title: {title}\nKeyword: {keyword}\nSocial Media Caption:")
])
social_media_chain = social_media_prompt_template | llm | output_parser

def run_chains(product_name, features, keyword):
    try:
        title = title_chain.invoke({"product_name": product_name, "features": features})
        description = description_chain.invoke({"title": title, "features": features})
        captions = social_media_chain.invoke({"title": title, "keyword": keyword})
        return title, description, captions
    except Exception as e:
        return None, None, f"An error occurred: {e}"

if st.button("Generate"):
    title, description, captions = run_chains(product_name, features, keyword)

    if title and description and captions:
        st.subheader("Generated Title:")
        st.markdown(f"<div class='generated-text'>{title}</div>", unsafe_allow_html=True)

        st.subheader("Generated Description:")
        st.markdown(f"<div class='generated-text'>{description}</div>", unsafe_allow_html=True)

        st.subheader("Generated Social Media Caption:")
        st.markdown(f"<div class='generated-text'>{captions}</div>", unsafe_allow_html=True)
    else:
        st.error(captions)

st.sidebar.header("Important Notes:")
st.sidebar.markdown(
    """
    1.  **Ollama Must Be Running:** Ensure Ollama is running in the background *before* running this Streamlit app.If not running then install the app from official website of Ollama
    2.  **Model Downloaded:** Make sure the specified model (`tinyllama` or `llama2:7b-chat-q4_0` etc.) is downloaded using `ollama pull <model_name>`.
    3.  **Memory Limits:**  This app is memory-intensive. Close other applications to free up memory if you encounter errors. If a small model still doesn't work, there may not be adequate free memory.
    4. **Model Selection:** The best results will come from models that meet your performance requirements while fitting your memory constraints. Experiment accordingly.
    """,
    unsafe_allow_html=True,
)