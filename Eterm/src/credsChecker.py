import sys
from smtplib import SMTP_SSL, SMTPAuthenticationError
from colorama import Fore


def check(email, password):
    with SMTP_SSL('smtp.gmail.com', 465) as session: # Make a session
        try:
            session.login(email, password) # Login to the server
        except SMTPAuthenticationError:# Incase of Password or email wrong or Anything else
            print("Allow less secure apps is in the OFF state by going to  "
                "https://myaccount.google.com/lesssecureapps . Turn it on and try again. "
                "make sure the Sender email & password are correct.")  
            sys.exit(f'{Fore.RED}[-] Wrong credentials{Fore.RESET}')

