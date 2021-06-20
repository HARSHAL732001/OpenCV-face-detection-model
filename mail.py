# Python code for sending mail from your Gmail account
import smtplib

# Creating SMTP Client Session
smtpobj = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security which makes the connection more secure
smtpobj.starttls()
senderemail_id="harshthakare732001@gmail.com"
senderemail_id_password="harshal7777777"
receiveremail_id="harshthakare70@gmail.com"

# Authentication for signing to gmail account
smtpobj.login(senderemail_id, senderemail_id_password)

# message to be sent
message = "Hello Sir Your Face is Recognized Successfully by our model !!"

# sending the mail - passing 3 arguments i.e sender address, receiver address and the message
smtpobj.sendmail(senderemail_id,receiveremail_id, message)

# Hereby terminate the session
smtpobj.quit()
print("Mail Send Successfully !! ")