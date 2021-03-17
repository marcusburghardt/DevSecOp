#!/usr/bin/python
# Python script useful to test mail servers settings and credentials.
#
# Created by Marcus Burghardt
# https://github.com/marcusburghardt/
import smtplib

# I am using these modules so is really easy to create HTML messages.
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import argparse
parser = argparse.ArgumentParser(description='Send standard messages via SMTP Server.')
parser.add_argument('-n', '--name', action='store',
                    default='Unknown',
                    help='Optional recipient name.')
parser.add_argument('-f', '--sender', action='store', default='sender@example.com',
                    help='Sender email address.')
parser.add_argument('-t', '--to', action='store', default='', required=True,
                    help='Recipient email address.')
parser.add_argument('-s', '--server', action='store', default='', required=True,
                    help='Server to be tested.')
parser.add_argument('-p', '--port', action='store', default='587',
                    help='Server port to connect. Usually 587, 465 or even 25.')
parser.add_argument('-u', '--username', action='store', default='', 
                    help='Username for authenticated session.')
parser.add_argument('-pw', '--password', action='store', default='',
                    help='Password for authenticated session.')

args = parser.parse_args()
SENDER_EMAIL = args.sender
RECIPIENT_NAME = args.name
RECIPIENT_EMAIL = args.to

SERVER = args.server
PORT = args.port
USERNAME = args.username
PASSWORD = args.password

def main():
    # set up the SMTP server
    s = smtplib.SMTP(host=SERVER, port=PORT)
    s.starttls()
    s.login(USERNAME, PASSWORD)

    msg = MIMEMultipart()
    message = "Test: "+SERVER+" is working!"
    # Setup the parameters of the message. You can explore more here, hum?
    msg['From']=SENDER_EMAIL
    msg['To']=RECIPIENT_EMAIL
    msg['Subject']="Test from "+SERVER
    #MIME-Version: 1.0
    
    # add in the message body
    msg.attach(MIMEText(message, 'html'))
    
    # send the message via the server set up earlier.
    s.send_message(msg)
    del msg
        
    # Terminate the SMTP session and close the connection.
    # This is not something critical since the timeout will close the connection
    # when the script finishes, but we like to do the things in the right way. :)
    s.quit()
    
if __name__ == '__main__':
    main()