import smtplib, ssl
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_txt_email(message,gm,pas,em):
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=ssl.create_default_context())
        server.ehlo()  # Can be omitted
        server.login(gm, pas)
        server.sendmail(gm,em, message)
def send_fancy_email(txt,html,gm,pas,em,sub):
    sender_email = gm
    receiver_email = em
    password = pas

    message = MIMEMultipart("alternative")
    message["Subject"] = sub
    message["From"] = sender_email
    message["To"] = receiver_email

        

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(txt, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)
 
