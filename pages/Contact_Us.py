import streamlit as st
import sendemail as send
st.header('Contact Us')

# Build contactUs form
with st.form("My Form", clear_on_submit=True):
    # st.write('Your email address:')
    user_email = st.text_input("Your email address: ",key='email')

    response_subject = st.text_input("Subject of the message ",key='subject', placeholder="Enter subject of the message here")

    # st.write('Your message to us:')
    user_response = f"""\
    Subject: {response_subject}\n
    
    {st.text_area(label="Your message to us: ",key="message", placeholder="Type your message to us")}
    """

    submitted = st.form_submit_button("Submit")
    print(submitted)
    if submitted:
        st.write('Submited')
        send.sendemail(user_email, user_response)
        st.info('Your email was sent successfully.')