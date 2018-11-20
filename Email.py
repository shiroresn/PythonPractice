
import smtplib

sender = 'shiroresn@gmail.com'
receivers = ['shubham.shirore@triarqhealth.com']

message = """From: From Person <shiroresn@gmail.com>
To: To Person <to@todomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""


   smtpObj = smtplib.SMTP('smtp.gmail.com')
   smtpObj.sendmail(sender, receivers, message)
   print ("Successfully sent email")
