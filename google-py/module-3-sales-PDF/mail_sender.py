#! /usr/bin/env python3

from email.message import EmailMessage
import os
import mimetypes
import smtplib
import getpass

# Ensure CWD is correct
print('CWD: ' + os.getcwd())

# Construct email details
sender = 'bigsock@hopmail.io'
recipient = 'mizo12free@largemail.com'
body = 'Mizo,\nWe had a back-up at the warehouse on Friday afternoon. A couple guys had to get re-routed and your job-order was placed in Roadside, NH. Apologies for the delay, the reroute for your package will arrive now by Wednesday at 2:00pm.\n-Joe'

message = EmailMessage()
message['From'] = sender
message['To'] = recipient
message['Subject'] = 'About that job order...'
message.set_content(body)
# print(message)

attachment_path = "./example.txt"
attachment_filename = os.path.basename(attachment_path)
mime_type, _ = mimetypes.guess_type(attachment_path)
print(mime_type)
mime_type, mime_subtype = mime_type.split('/', 1)
print(mime_type)
print(mime_subtype)

with open(attachment_path, 'rb') as ap:
	message.add_attachment(ap.read(),
		maintype=mime_type,
		subtype=mime_subtype,
		filename=os.path.basename(attachment_path))
# print(message)

# Mail Server Set-up
mail_server = smtplib.SMTP_SSL('example.mail.com')
mail_server.set_debuglevel(1)
mail_pass = getpass.getpass('Password? ')

# Login Attempt
mail_server.login(sender, mail_pass)

# Send Email
mail_server.send_message(message)
mail_server.quit()
