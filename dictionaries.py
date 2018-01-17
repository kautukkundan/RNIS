#initialize empty dictionary
graph = { }  



#initialize dictionary with key value pairs
#put comma after every pair
graph = {
	'key1' : 'value',	#string value
	'key2' : 1,			#int value
	'key3' : [1,2,3],	#list value 
	'key4' : 'value',	#another string
	
	'key5' : {
		'nested1' : 'dict within dict'  #nested dictionary
	}
}



#print dictionary
print graph



#access a value of dictionary
print graph['key1']
print graph['key3']



#add key value pair to dictionary
graph['new1'] = 123
graph['new2'] = 'al habibi wallah walla'
print graph



#delete element from dict
del graph['new1']




#accessing nested lists and dictionaries

print graph['key3'][1]
#value at key 3 is a list and we are printing the element at index 1 of list


print graph['key5']['nested1']
#accessing key of nested dictionary