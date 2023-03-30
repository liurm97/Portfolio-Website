# smtplib > send email
# ssl > Authentication with server
import smtplib, ssl

USERNAME = "app1sendemail@gmail.com"
PASSWORD = "vhsoelaqqsjuvigr"
ENV = "smtp.gmail.com"
PORT= 465

def sendemail(recipient, message):
    """
    Send email to `recipient` in the gmail domain with content of the message = `message`
    """
    # Create secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(ENV, port=PORT, context=context) as server:

        # Login to gmail email server
        server.login(USERNAME, PASSWORD)

        # Use gmail email server to send email
        server.sendmail(to_addrs=recipient, msg=message, from_addr=USERNAME)

if __name__ == "__main__":
    pass