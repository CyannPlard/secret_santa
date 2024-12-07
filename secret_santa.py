import random
import smtplib, ssl

def send_email(receiver_email: str, message: str)->None:
    smtp_server = "smtp.serveur.serveur"
    port = 587  # For starttls
    sender_login = "login"
    sender_email = "email@email.email"
    password = 'password'

    # Create a secure SSL context
    context = ssl.create_default_context()

    theme = "Pere & mere noel secret.e"
    msg = f'From: {sender_email}\r\nTo: {receiver_email}\r\nContent-Type: text/plain; charset="utf-8"\r\nSubject: {theme}\r\n\r\n'    
    msg += message + " aura la chance de recevoir ton cadeau !"

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_login, password)
        server.sendmail(sender_email, receiver_email, msg.encode('utf8'))
        
    except Exception as e:
        print(e)
    finally:
        server.quit()

dict_address = {'Name1' : 'name1.email@email.email',
                'Name2' : 'name2.email@email.email',
                'Name3' : 'name3.email@email.email',
               }
                
names=dict_address.keys()
names2=list(names).copy()

santa_names = {}
for name in names:
    santa = random.choice([n for n in names2 if n is not name])
    santa_names.update({name : santa})
    names2.remove(santa)
    
for name in dict_address :
    receiver_email = dict_address[name]
    message = santa_names[name]
    #send_email(receiver_email,message)
    print(receiver_email,message)