cars = ['honda', 'maruti', 'toyota', 'hyundai', 'datsun', 'BMW', 'audi']


#find length of list
print len(cars)



#print list in a range
print cars[2:4]
#prints elements from 2nd to 4th index 



#print lists UPTO an index
print cars[:3]
#prints elements till 3rd place



#print element FROM an index till last
print cars[3:]
#prints elements from 3rd place


#check if any element is in list
print ('BMW' in cars)
print ('Renault' in cars)


#FOR LOOP
for i in range(0,12,1):
	print i
	
#   for (initial value, final value, step increment):
#   if starting from 0th, no need to give initial value



#Iterate elements INDEX-WISE
for i in range(len(cars)):
	print cars[i]