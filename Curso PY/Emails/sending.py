import smtplib, getpass, imaplib

# autenticando
smtp_object = smtplib.SMTP('smtp.gmail.com',587)
smtp_object.ehlo()
smtp_object.starttls()

try:
    email = input("Email: ")
    password = getpass.getpass('Senha: ')
    print(smtp_object.login(email, password))
except:
    print("Algo deu errado.")
else:
    print("Logado com sucesso.")

from_address = email
to_address = input("Email de destino: ")
subject = input("Assunto: ")
message = input("Mensagem: ")
full_msg = "Subject: "+subject+'\n'+message

try:
    smtp_object.sendmail(from_address,to_address,full_msg)
    smtp_object.quit()
except:
    print("Algo deu errado.")
else:
    print("Mensagem enviada com sucesso.")