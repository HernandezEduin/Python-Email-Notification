# Python-Email-Notification
Simple and handy functions for sending email notifications when simulations are done running.

To use this code with a gmail account, you must manually [allow a less secure access](https://myaccount.google.com/lesssecureapps) by turning the switch ON to give Python access to your account. If you don’t change this setting, when running the code later, you’ll get an error message like below:

    SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials - gsmtp')

For safety concerns, it is not recommended to connect using your personal email.

You can setup and modify your email configurations in email_cofig.ini so you don't need to enter them each time.
