import smtplib
import getpass
# send mail
smtp_object = smtplib.SMTP('smtp.gmail.com', 587) # TLS
smtp_object.ehlo()

# SSL Port 465
# TLS Port 587

smtp_object.starttls()
email = getpass.getpass('Please enter your email: ')

#
password = getpass.getpass('Please enter your password: ')

print(smtp_object.login(email, password))

sender = getpass.getpass('Please enter your email: ')
receiver = getpass.getpass('Please enter the email of the receiver: ')
subject = input('Subject: ')
message = input('Message: ')

complete = 'Subject: ' + subject + '\n' + message
print(smtp_object.sendmail(sender, receiver, complete))


