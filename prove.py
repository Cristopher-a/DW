import ssl
import smtplib
from email.message import EmailMessage
import random

number=random.randint(1000,9999)


remitente = 'desarrolloweb4775@gmail.com'
contrasena = 'hefa qcdb vaed zrch'
destinatario = 'crisesv4@gmail.com'

asunto = 'Recuperar contraseña'


em = EmailMessage()
em['From'] = remitente
em['To'] = destinatario
em['Subject'] = asunto
em.set_content(str(number))  

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(remitente, contrasena)
    smtp.sendmail(remitente, destinatario, em.as_string())