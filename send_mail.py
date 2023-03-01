EMAIL_HOST='smtp.titan.email'
EMAIL_HOST_USER='admin@test.com'
EMAIL_HOST_PASSWORD='password'  
EMAIL_PORT= 465
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_SSL=True

ADMIN_EMAIL = "admin@test.com"
SUPPORT_EMAIL = "admin@test.com"
DEFAULT_FROM_EMAIL = ADMIN_EMAIL
SERVER_EMAIL = ADMIN_EMAIL

import smtplib
import ssl
from email.mime.text import MIMEText

smtp_server = "smtp.titan.email"
smtp_port = 465
sender = "xyz@abc.com"
password = "XXXXXXX"
recipients = ["hello@abc.com"]

context = ssl.create_default_context()

s = smtplib.SMTP_SSL(smtp_server, smtp_port, context)
s.set_debuglevel(1)

s.ehlo()
s.login(sender, password)

msg = MIMEText("""Hey, this is test body""")
msg['From'] = sender
msg['To'] = ", ".join(recipients)
msg['Subject'] = "test subject"
s.sendmail(sender, recipients, msg.as_string())
s.close()

