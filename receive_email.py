import imaplib
import email
import getpass
from select import select

conn = imaplib.IMAP4_SSL('imap.gmail.com')

# login
user = getpass.getpass('Enter your email: ')
password = getpass.getpass('Enter your password: ')
login_result = conn.login(user, password)
print(f'login_result: {login_result}')

if login_result[0] == 'OK':
    # print mailboxes
    print(conn.list())

    select_result = conn.select('inbox')

    if select_result[0] == 'OK':
        # imaplib.MAXLINE = 1000000
        #typ, data = conn.search(None, 'SUBJECT "Hallo Python"')
        #typ, data = conn.search('utf-8', "FROM mawielan@gmail.com".encode('utf-8'))
        typ, data = conn.search(None, 'BEFORE 01-Nov-2024')

        if typ == 'OK': # Data received
            for dat in data[-1].split():
                result, email_data = conn.fetch(dat, '(RFC822)')
                email_content = email_data[0][1]
                email_text = email_content.decode('utf-8')
                #print(email_text)
                email_message = email.message_from_string(email_text)
                for teil in email_message.walk():
                    if teil.get_content_type() == 'text/plain':
                        body = teil.get_payload(decode=True)
                        print(body)



