#empty list initialization
cars = []   



#list initialization with values
cars = ['honda', 'maruti', 'toyota']



#printing list
print cars



#adding elements to list
cars.append('hyundai')
print cars



#removing element from list
last_elem = cars.pop()
print last_elem
print cars



#accessing element at a particular index
print cars[1]
print cars[2]



#adding element at a particular index
cars.insert(1,'datsun')
print cars



#removing a particular element
cars.remove('honda')



#merging two lists
sports_cars = ['lamborghini', 'ferrai', 'masserati']
cars.extend(sports_cars)
#OR
cars = cars + sports_cars
print cars



#list reverse
cars.reverse()
print cars




#list sorting
nums = [3,6,1,43,5,57,56,8]
nums.sort()
print nums



#list sorting (descending)
nums = [3,6,1,43,5,57,56,8]
nums.sort(reverse=True)
print nums