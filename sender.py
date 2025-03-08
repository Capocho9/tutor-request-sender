from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def contact_tutors(subject,level,availability,email,tutors):
  availability = ' ' + ', '.join(availability)
  
  try:
    server = SMTP('smtp.gmail.com', 587)

    server.starttls()
      
    server.login('ajhomicz@gmail.com', 'ukfw yhks jibd nnhu')
    
    msg = MIMEMultipart()
    
    msg['Subject'] = "Tutor Request"
    
    content = f'Hello, a student has requested a tutor for {subject} at the {level} level. They are available to meet at the following times:{availability}.\n\nIf you are interested, please contact them at {email}.'
      
    msg.attach(MIMEText(content,'plain'))
    
    mail = msg.as_string()

    for tutor in tutors:
    
      server.sendmail('ajhomicz@gmail.com',tutor, mail)
    
    server.quit()
  
  except Exception as error:
    print(f'An error occured: {error}')