import streamlit as st
from PIL import Image

# Set page config with improved icon & layout
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🚀", layout="wide")

# Custom CSS for Styling
def load_css():
    st.markdown(
        """
        <style>
            .main {background-color: #f5f7fa;}
            .header {color: #2C3E50; font-size: 36px; text-align: center; font-weight: bold;}
            .subheader {color: #34495E; font-size: 24px; text-align: center;}
            .quote {color: #1ABC9C; font-size: 20px; text-align: center; font-style: italic;}
            .footer {text-align: center; margin-top: 50px; color: #7F8C8D; font-size: 16px;}
        </style>
        """,
        unsafe_allow_html=True,
    )
load_css()

# App Title
st.markdown("<div class='header'>Growth Mindset Challenge 🌱</div>", unsafe_allow_html=True)
st.markdown("<div class='subheader'>Unlock your full potential with reflection, challenges & achievements</div>", unsafe_allow_html=True)

st.markdown("---")

# Quote Section
st.markdown("<div class='subheader'>📖 Today's Growth Mindset Quote</div>", unsafe_allow_html=True)
st.markdown("<div class='quote'>✨ 'Success is not final, failure is not fatal: it is the courage to continue that counts.' - Winston Churchill</div>", unsafe_allow_html=True)

st.markdown("---")

# Challenge Input
st.markdown("### 🎯 What's your Challenge Today?")
user_input = st.text_input("Describe a challenge you are facing:")
if user_input:
    st.success(f"You're facing: {user_input}. Keep pushing forward! 💪")
else:
    st.warning("Tell us about your challenge to get started! 📝")

# Reflection Section
st.markdown("### 🤔 Reflect on your Learning")
reflection = st.text_area("Write your reflections here:")
if reflection:
    st.success(f"Great Insight! Your reflection: {reflection} ✨")
else:
    st.info("Reflecting on your past experience helps you grow! 🚀")

# Achievements Section
st.markdown("### 🏆 Celebrate your Wins!")
achievement = st.text_input("Share something you've recently accomplished:")
if achievement:
    st.success(f"Amazing! You achieved: {achievement} 🎉")
else:
    st.info("Big or small, every achievement counts! Share one now! 😊")

# Footer Section
st.markdown("<div class='footer'>Keep believing in yourself. Growth is a journey, not a destination! 🌍</div>", unsafe_allow_html=True)
st.markdown("<div class='footer'><b>🚀 Created by Khizra Irfan</b></div>", unsafe_allow_html=True)