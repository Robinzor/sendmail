import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


mail_content = str("Test")
# The mail addresses and password
sender_address = 'username@domain.nl'
sender_pass = 'password'
receiver_address = ('username@domain.nl')
# Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = "Test"
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.office365.com', 587)
session.starttls() #enable security
session.login(sender_address, sender_pass)
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')

