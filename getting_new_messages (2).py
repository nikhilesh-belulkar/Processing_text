##simply looking through the emails and making a document
## that contains all the messages and email ID's for the new messages 
import imaplib, email
import utilities 
import csv 


username = 'cmckeon@cbmpartners.co'
password = 'Zachman246'
imapurl = 'imap.gmail.com'

con = imaplib.IMAP4_SSL(imapurl)
con.login(username, password)
con.select('INBOX')


new_messages = {}


tmp, data = con.search(None, '(UNSEEN)')

filename = "ID_cmckeon@cbmpartners.csv"


for emailnum in data[0].split():
    result, data = con.fetch(emailnum,'(RFC822)')
    raw = email.message_from_bytes(data[0][1])
    print(emailnum)
    try:
        if(utilities.get_sender(str(raw))!=username):
            msg  = str(utilities.refineMSG(str(utilities.get_body(raw))))[2:]
            with open(filename, 'w') as f:
                    f.write("%s,%s,%s\n"%(emailnum,msg,utilities.get_sender(str(raw))))
    except:
        continue











