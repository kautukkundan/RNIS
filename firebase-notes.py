from firebase import firebase  	#imports firebase module
from sys import argv			#imports argv for taking arguments

operation = argv[1]				#gets argument inside code

if (len(argv)>2):				#checks if note available
	note = argv[2]



firebase = firebase.FirebaseApplication("URL_OF_YOUR_DATABASE") 	#initialize firebase app


if(operation=='fetch'):

	#FETCHES THE ENTIRE DATABASE FROM FIREBASE (dictionary format)
	res = firebase.get('/', None) 
	
	#prints the dictionary elementwise
	for key in res:
		print res[key]



elif(operation=='add'):

	#ADDS AN ELEMENT TO THE DATABASE
	res = firebase.post('/', note)
	
	#prints confirmation
	print 'Note added successfully'



elif(operation=='delete'):

	#FETCHES THE ENTIRE DATABASE FROM FIREBASE (dictionary format)
	res = firebase.get('/', None)

	#finds mathing key in database
	for key in res:
		
		#Finds the corresponding key
		if (res[key]==note):

			#removes that key from database
			firebase.delete('/',key)

	#prints confirmation		
	print 'Note deleted successfully'



else:
	print("invalid command")
