import streamlit as st
import streamlit.components.v1 as com

with open("styleing.css") as source:
    design=source.read()
st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align:center;color: rgb(65, 64, 64);font-size:70px; background-color:white;'>About Us</h1>",unsafe_allow_html=True)

# st.image("./images/About_Us.png",width=1755)
st.image("./images/heart.png",width=1755)

st.markdown("<h1 style='text-align:center; color:purple; font-size:50px; background-color:white;'>Our Team Members</h1>",unsafe_allow_html=True)

com.html(f"""
 <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
 <link rel="stylesheet" href="./style.css">
 <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
    <style>
         {design}
    </style>
<body>
    <div class="card">
        <div class="card-image">
            # <img src="./images/Profile1.png" alt="Profile-Image">
            <img src="https://i.ibb.co/RjBMLTx/Aradhya-Profile1.png" id="img">
            # st.image("./images/Profile1.png")
        </div>
        <p class="name">Aradhya Solanki</p>
        <p>UI / UX Developer</p>
        <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Dignissimos earum ullam aliquam minima non. Excepturi maiores eaque voluptatum eius sapiente.</p>
        <div class="socials">
            <a href="https://github.com/Aradhya321">
                <button class="github"><i class="fab fa-github"></i></button>
            </a>
            <a href="https://twitter.com/AradhyaSolanki?t=J17YDjfmyWJ21oN5OD9uGw&s=09">
                <button class="twitter"><i class="fab fa-twitter"></i></button>
            </a>
            <a href="https://www.linkedin.com/in/aradhya-solanki-2573791b9">
                <button class="linkedin"><i class="fab fa-linkedin"></i></button>
            </a>
        </div>
    </div>
    <div class="card">
        <div class="card-image">
            #  <img src="./images/Profile1.png" alt="Profile-Image">
            <img src="https://cdn1.vectorstock.com/i/1000x1000/23/70/man-avatar-icon-flat-vector-19152370.jpg" id="img">
        </div>
        <p class="name">Himanshu Gehlot</p>
        <p>UI / UX Developer</p>
        <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Dignissimos earum ullam aliquam minima non. Excepturi maiores eaque voluptatum eius sapiente.</p>
        <div class="socials">
            <a href="https://github.com/Aradhya321">
                <button class="github"><i class="fab fa-github"></i></button>
            </a>
            <a href="https://twitter.com/AradhyaSolanki?t=J17YDjfmyWJ21oN5OD9uGw&s=09">
                <button class="twitter"><i class="fab fa-twitter"></i></button>
            </a>
            <a href="https://www.linkedin.com/in/aradhya-solanki-2573791b9">
                <button class="linkedin"><i class="fab fa-linkedin"></i></button>
            </a>
        </div>
    </div>
    <div class="card">
        <div class="card-image">
            #  <img src="./images/Profile1.png" alt="Profile-Image">
            <img src="https://cdn1.vectorstock.com/i/1000x1000/23/70/man-avatar-icon-flat-vector-19152370.jpg" id="img">
        </div>
        <p class="name">Pranay Vyas</p>
        <p>UI / UX Developer</p>
        <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Dignissimos earum ullam aliquam minima non. Excepturi maiores eaque voluptatum eius sapiente.</p>
        <div class="socials">
            <a href="https://github.com/Aradhya321">
                <button class="github"><i class="fab fa-github"></i></button>
            </a>
            <a href="https://twitter.com/AradhyaSolanki?t=J17YDjfmyWJ21oN5OD9uGw&s=09">
                <button class="twitter"><i class="fab fa-twitter"></i></button>
            </a>
            <a href="https://www.linkedin.com/in/aradhya-solanki-2573791b9">
                <button class="linkedin"><i class="fab fa-linkedin"></i></button>
            </a>
        </div>
    </div>
    
    <div class="card">
        <div class="card-image">
            #  <img src="./images/Profile1.png" alt="Profile-Image">
            <img src="https://cdn1.vectorstock.com/i/1000x1000/23/70/man-avatar-icon-flat-vector-19152370.jpg" id="img">
        </div>
        <p class="name">Suyog Sinnarkar</p>
        <p>Front-End Developer</p>
        <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Dignissimos earum ullam aliquam minima non. Excepturi maiores eaque voluptatum eius sapiente.</p>
        <div class="socials">
            <button class="github"><i class="fab fa-github"></i></button>
            <button class="twitter"><i class="fab fa-twitter"></i></button>
            <button class="linkedin"><i class="fab fa-linkedin"></i></button>
        </div>
    </div>
    <div class="info">
    <h2> Disclaimer: The information on OnlineHeartRate.com is not intended to be a substitute for professional medical advice. Talk with your healthcare provider about any questions you may have regarding a medical condition.</h2>
    <h2><br>© 2023 www.OnlineHeartRate.com | All rights reserved.</h2>
    </div>
</body>
""",height=1000, width=1754)