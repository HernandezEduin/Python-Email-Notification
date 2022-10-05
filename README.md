# Python-Email-Notification
Simple and handy functions for sending email notifications when simulations are done running.

To use this code with a gmail account, you must set a 2-step verification and then generate an App Password, for more information refer to [Create & use App Passwords](https://support.google.com/accounts/answer/185833). The App Password is the 16-character code in the yellow bar on your device. Copy this password into the email_config.ini file. If you don’t change this setting, when running the code later, you’ll get an error message like below:

    SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials - gsmtp')

For safety concerns, it is not recommended to connect using your personal email.

You can setup and modify your email configurations in email_cofig.ini so you don't need to enter them each time.
