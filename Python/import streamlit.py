import streamlit as st

st.title("Welcome to My System by Sayed Hamza")

user_id = "mazi_ashmi02"
password = "1234"

u = st.text_input("Enter your username:")
p = st.text_input("Enter your password:", type="password")

if st.button("Login"):
    if user_id == u and password == p:
        st.success("Welcome to My system! by Sayed Hamza")

        a = st.text_input("Hi there what's up?")
        if a:
            st.write("I am happy to hear that you are doing well!")
            st.write("Thank you for sharing your feelings with me!")

            b = st.text_input("Tumhara naam kya hai?")
            if b:
                st.write("My name is Sayed Hamza!")
                st.write("Mil kar acha laga")
                st.write("Sayed Hamza ka naam le lo, aur chalo khush raho!")

            sm = st.text_input("Apki bhabhi ka naam kya hai?")
            if sm:
                st.write("'Sayeda Muskan Hamza ki Jaan'")
                st.write("Pura naam lo beta ji!")

            st.markdown("---")
            st.write("Aaj ke liye itna hi, Fi amanillah!")
            st.write("Aur han 'Next time bhabhi ka naam sahi se lena!!!'")

    else:
        st.error("Hieght ke sath dimag bhi badha le Gadhi ladki")
