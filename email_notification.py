# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 15:24:47 2022

@author: Eduin Hernandez
Summary: Simple implementation to send an email notification. Useful for being notified when simulations are done.
"""

import smtplib, ssl
from configparser import ConfigParser

def send_email(sender: str, password: str, receiver: str, content:str, subject:str="") -> None:
    "Sends the email to the specified receipient"
    try:
        # Connect to the Gmail SMTP server and Send Email
        # Create a secure default settings context
        context = ssl.create_default_context()
        
        # Connect to Gmail's SMTP Outgoing Mail server with such context
        if len(subject) != 0:
            content = "Subject: " + subject + "\n" + content
        
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            # Provide Gmail's login information
            server.login(sender, password)
            # Send mail with from_addr, to_addrs, msg, which were set up as variables above
            server.sendmail(sender, receiver, content)
    except:
        print("Failed notification status!")

def load_email_config(path:str = "./email_config.ini"):
    """"Returns email configurations set by the user. Must contain a section titled email
        and the following 3 keys: sender (your email), password (belonging to your email),
        and receiver (who do want to send it to). Check email_config.in for the syntax.
    """
    parser = ConfigParser()
    try:
        parser.read(path)
        
        sender = parser.get("email", "sender")
        receiver = parser.get("email", "receiver")
        password = parser.get("email", "password")
        
        email_config = {'sender': sender,
                  'receiver': receiver,
                  'password': password}
        return email_config
    except:
        assert False, "Error in the configurations!"

    
    
if __name__ == '__main__':
    'Sample code to load email configurations and send an automatic email.'
    email_config = load_email_config("./email_config.ini")
    
    email_subject = 'Testing Configurations'
    email_string = 'This is a test email sent from python'

    send_email(email_config['sender'], email_config['password'],
               email_config['receiver'], email_string, email_subject)