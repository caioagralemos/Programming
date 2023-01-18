import email, getpass, imaplib

email = input("Email: ")
password = getpass.getpass('Senha: ')
subject = input("Assunto que vamos procurar: ")

M = imaplib.IMAP4_SSL('imap.gmail.com')
M.login(email, password)
M.select('Inbox')

typ, data = M.search(None, f'SUBJECT "{subject}"')
print(typ)
email_id = data[0]
result, email_data = M.fetch(email_id, '(RFC822)')

raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')

print(raw_email_string)