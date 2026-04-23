import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="Viral Score", page_icon="🔥", layout="centered")
st.title("🔥 Viral Score")
st.caption("TikTok's favourite video idea rater • Get your score in seconds")

idea = st.text_area("Your video idea (be as detailed as you want)", 
                    placeholder="POV: You're a barista and the customer orders the most complicated drink ever...", 
                    height=150)

if st.button("🚀 Get My Viral Score", type="primary", use_container_width=True):
    if not idea.strip():
        st.warning("Please enter a video idea!")
    else:
        score = random.randint(72, 98)
        keywords = ["duet", "trend", "sound", "transition", "grwm", "pov", "asmr", "hack", "before after", "challenge"]
        boost = sum(1 for word in keywords if word.lower() in idea.lower())
        score = min(98, score + boost * 3)

        st.success(f"**Your Viral Score: {score}/100** 🔥")

        col1, col2, col3 = st.columns(3)
        with col1: st.metric("Hook Strength", f"{random.randint(75,99)}%")
        with col2: st.metric("Trend Fit", f"{random.randint(70,99)}%")
        with col3: st.metric("Shareability", f"{random.randint(80,99)}%")

        st.subheader("💡 Pro Tips to Go Viral")
        for tip in ["Strong hook in first 3s", "Use trending sound", "Big text on screen", "Vertical 9:16", 
                    "Post at peak times", "Strong CTA at the end"]:
            st.write("• " + tip)

        st.info("Screenshot this and post it on TikTok — it drives tons of traffic!")

st.caption("Made for TikTok creators • Share this app!")
