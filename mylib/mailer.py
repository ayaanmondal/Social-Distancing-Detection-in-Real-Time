import smtplib, ssl

class Mailer:

    """
    This script initiaties the email alert function.
    """
    def __init__(self):
        # Enter your email below. This email will be used to send alerts.
        # E.g., "email@gmail.com"
        self.EMAIL = "csayan.py@gmail.com"
        # Enter the email password below. Note that the password varies if you have secured
        # 2 step verification turned on. You can refer the links below and create an application specific password.
        # Google mail has a guide here: 
        # For 2 step verified accounts: 
        # Example: aoiwhdoaldmwopau
        self.PASS = "gpdjlsfzdjkivqjq"
        self.PORT = 465
        self.server = smtplib.SMTP_SSL('csayan.py@gmail.com', self.PORT)

    def send(self, mail):
        self.server = smtplib.SMTP_SSL('csayan.py@gmail.com', self.PORT)
        self.server.login(self.EMAIL, self.PASS)
        # message to be sent
        SUBJECT = 'ALERT!'
        TEXT = f'Social distancing violations exceeded!'
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

        # sending the mail
        self.server.sendmail(self.EMAIL, mail, message)
        self.server.quit()
