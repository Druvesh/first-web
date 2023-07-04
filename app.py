import streamlit as st

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/ 
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# Use Local CSS 
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")






# ---- HEADER SECTION ----
st.subheader("Hi, I am Druvesh :wave:")
st.title("My First Webpage")
st.write("[Learn More >](https://www.youtube.com/watch?v=dQw4w9WgXcQ)")


# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/druvesh14@gmail.com" method="POST">
    <input type= "hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column: 
    st.empty()
























