import os
import streamlit as st
import requests
import datetime

API_KEY = "4190189464944ecf9995818b0d3e3854"


st.set_page_config(page_title="Weather App", page_icon="🌤️", layout="centered")

st.markdown(
    """
    <style>
    .weather-container {
        max-width: 500px;
        margin: auto;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        background: white;
        text-align: center;
    }
    .temperature {
        font-size: 45px!important;
        font-weight: bold;
        color: #ff7b00;
    }
    .info {
        font-size: 20px;
        font-weight: 500;
    }
    .footer {
        margin-top: 30px;
        font-size: 16px;
        color: gray;
        text-align: center;
    }
    </style>
    """
    ,
    unsafe_allow_html=True,
)

# st.markdown('<div class="weather-container">', unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #fff;'>🌤️ Weather App</h1>", unsafe_allow_html=True)

city = st.text_input("Enter city name:", placeholder="Enter city name ...")

if st.button("Get Weather"):
    if city:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise']).strftime('%I:%M %p')
            sunset = datetime.datetime.fromtimestamp(data['sys']['sunset']).strftime('%I:%M %p')

            st.markdown(f"<h2 style='color: #007bff; text-align: center; font-weight: bold;'>Weather in {city} 🌡</h2>", unsafe_allow_html=True)
            st.markdown(f"<p class='temperature'>{data['main']['temp']}°C</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='info'>🌬️ Wind Speed: {data['wind']['speed']} m/s</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='info'>☁️ Condition: {data['weather'][0]['description'].capitalize()}</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='info'>🌅 Sunrise: {sunrise}</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='info'>🌇 Sunset: {sunset}</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='info'>💧 Humidity: {data['main']['humidity']}%</p>", unsafe_allow_html=True)

        else:
            st.error("❌ City not found. Please try again.")
    else:
        st.warning("⚠️ Please enter a city name.")

st.markdown('<p class="footer">Name: <b>Huzaifa</b> | Roll Number: <b>499351</b></p>', unsafe_allow_html=True)