import smtplib 		#SIMPLE MAIL TRANSFER PROTOCOL

#Content of the email
content = 'example email stuff here' 	

#initilize the module with service and port number
mail = smtplib.SMTP('smtp.gmail.com', 587)

#identify yourself to the server
mail.ehlo()

#enable encrypted login and message sending
#TLS = transport layer security
mail.starttls()

#login to your account
mail.login('YOUR-EMAIL-ADDRESS', 'YOUR-PASSWORD')

#create and send mail
mail.sendmail('FROM','TO',content)

#finish the process 
mail.close()