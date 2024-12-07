import random
import smtplib, ssl
import yaml

def send_email(receiver_email: str, name: str)->None:
    """
    Envoie un email à un.e destinataire spécifique pour lui communiquer le nom de la personne
    à qui iel devra offrir un cadeau dans le cadre du Père ou Mère Noël Secret.e.
    (Sends an email to a specified recipient informing them of their Secret Santa match.)

    Parameters:
        receiver_email (str):  Adresse email du destinataire. (The recipient's email address.)
        name (str): Nom de la personne à qui offrir un cadeau. (The name of the person they will give a gift to.)
    """
        
    with open('config.yml', 'r') as f:
        config = yaml.load(f, Loader=yaml.SafeLoader)
    context = ssl.create_default_context()
    sender_email = config['sender_email']

    theme = "Pere & mere noel secret.e"
    msg = f'From: {sender_email}\r\nTo: {receiver_email}\r\nContent-Type: text/plain; charset="utf-8"\r\nSubject: {theme}\r\n\r\n'    
    msg += name + " aura la chance de recevoir ton cadeau !"
    try:
        server = smtplib.SMTP(config['smtp_server'], config['port'])
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(config['sender_login'], config['password'])
        server.sendmail(config['sender_email'], receiver_email, msg.encode('utf8'))
        
    except Exception as e:
        print(e)
    finally:
        server.quit()

# Charge les informations des participant.e.s depuis le fichier yml
# Load participant information from yml file
with open('info_participant(e)s.yml', 'r') as f:
    dict_address = yaml.load(f, Loader=yaml.SafeLoader)
names=dict_address.keys()

# Attribuer de manière aléatoire chaque participant à un Père Noël Secret
# Randomly assign each participant a Secret Santa recipient who is not the given participant
names2=list(names).copy()
santa_names = {}
for name in names:
    santa = random.choice([n for n in names2 if n is not name])
    santa_names.update({name : santa})
    names2.remove(santa)

# Notifier chaque participant de leur attribution par email
# Notify each participant of their Secret Santa assignment via email
for name in dict_address :
    receiver_email = dict_address[name]
    happy_name = santa_names[name]
    send_email(receiver_email,happy_name)
    #print(f'{receiver_email}:{happy_name})