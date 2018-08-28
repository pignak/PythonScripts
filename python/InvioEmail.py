import smtplib

contenuto = 'il contenuto della mia email'
mail = smtplib.SMTP('smtp.gmail.com', 587) # questa configurazione funziona per gmail
mail.ehlo() # protocollo per extended SMTP
mail.starttls() # email criptata
mail.login("tuaemail", "tuapassword")
mail.sendmail('tuaemail', 'emaildestinatario', contenuto)
mail.close()