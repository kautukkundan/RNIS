graph = {
	'sdfadf12112' : 'value',	#string value
	'kesadfsdfy2' : 1,			#int value
	'ke2ecdsfay3' : [1,2,3],	#list value 
	'key1242345f' : 'value',	#another string
	
	'key321casd5' : {
		'nested1' : 'dict within dict'  #nested dictionary
	}
}



#for loop
for key in graph:
	print graph[key]


#iterates through all the keys in the dictionary without knowing the actual value

#creates a variable placeholder named "key"

#sends this variable in dictionary

#puts the value of first encountered key in place of "key"

#prints the value of that key

#loops