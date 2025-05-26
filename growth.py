#streamlit
import streamlit as st 

st.set_page_config(page_title = "growth mindset project", page_icon = "✨")
st.title(" Growth Mindset Challenge: Web App with Streamlit ")
st.header("🚀 Welcome to Your Growth Journey! ")
st.write(" Embrace challenges, learn from mistakes and unlock your full potential. This AI-powered app helps you build a growth mindset with reflection, challenges and achievements! ")
#quote section
st.header("💡 Today's Growth Mindset Quote ")
st.write(" “Success is not final, failure is not fatal, it is the courage to continue that counts.″ — Winston Churchill ")
st.header(" What's Your Challenge Today ❔ ")
user_input = st.text_input(" Describe a challenge you are facing: ")
#condition
if user_input:
    st.success(f" You are facing: {user_input}. Keep pushing forward towards your goal! ")
else:
    st.warning(" Tell us about your challenge to get started! ")
#reflexing
st.header(" Reflect on your Learning ")
reflection = st.text_area(" Write your reflections here: ")
if reflection:
    st.success(f"🎇Great Insight! Your reflection: {reflection} ")
else:
    st.info("Reflecting on past experience help you grow! Share your  difficulties ")
#achievements
st.header("🏆 Celeberate Your Wins! ")
achievment = st.text_input(" Share something you have recently accomplished: ")
if achievment:
    st.success(f" 👍Amazing! You achieved: {achievment} ")
else:
    st.info(" Big or small,  every achievement counts!  Share one now 🌈 ")
#footer
st.write("- - -")

st.write(" 🚀Keep believing in yourself. Growth is a journey, not a destination! 🌟")
st.write(" *⚡*Created by Mahwish*⚡* ")        