import streamlit as st

st.set_page_config(page_title="My Contacts", page_icon="🎂", layout="wide")

def main():
    st.title("Survey")

    # Frage 1
    st.subheader("Question 1: What is your favorite color?")
    color_options = ["Red", "Blue", "Green", "Yellow"]
    color = st.radio("Select your favorite color:", color_options)

    # Frage 2
    st.subheader("Question 2: How many hours do you spend coding per week?")
    hours_coding = st.slider("Select the number of hours:", min_value=0, max_value=100, step=1, value=20)

    # Frage 3
    st.subheader("Question 3: Do you prefer cats or dogs?")
    pet_preference = st.selectbox("Select your preference:", ["Cats", "Dogs"])

    # Frage 4
    st.subheader("Question 4: What is your age?")
    age = st.number_input("Enter your age:", min_value=0, max_value=150, value=30)

    # Frage 5
    st.subheader("Question 5: What country are you from?")
    country = st.text_input("Enter your country:")

    # Button zum Absenden der Umfrage
    if st.button("Submit"):
        # Ergebnisse anzeigen
        st.success("Survey Submitted Successfully!")
        st.write("Your favorite color:", color)
        st.write("Hours spent coding per week:", hours_coding)
        st.write("Pet preference:", pet_preference)
        st.write("Your age:", age)
        st.write("Your country:", country)

if __name__ == "__main__":
    main()