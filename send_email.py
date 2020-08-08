import smtplib
from email.message import EmailMessage

# function to send email to listed email address 
def send_email(info,news):
    email = EmailMessage()
    email['From'] = '< Sender Name >'
    email['To'] = info[1]
    email['Subject'] = 'Hello '+info[0]
    email.set_content(news,'html')
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('<Sender Email>','<Sender Password>')
        smtp.send_message(email)
        smtp.quit()