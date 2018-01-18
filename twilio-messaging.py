from twilio.rest import Client 		#import Client module from twilio.rest

account_sid = "INSERT_SID"					#insert your own account_sid you'll get from twilio website
	
auth_token = "INSERT_TOKEN"					#insert your own auth_token you'll get from twilio website
	
client = Client(account_sid, auth_token)	#initialize an instance of Client module

#actual message body 

message = client.api.account.messages.create(
	to="RECEIVERS_PHONE_NUMBER",
	from_="OBTAINED_PHONE_NUMBER", 
	body= "test_message"
)

print message.sid 			#returns the transaction SID