import math

#Test lists 5 dimension
list1 = [5,1,2,6,2]
list2 = [1,3,5,0,3]
list3 = [5,1,2,6,2]
list4 = [99,99,99,99,99]
list5 = [5,-1,-2,-4,2]

def similarity(a,b):
	d = 0
	zipped = zip(a,b)
	
	for x, y in zipped:
		if x < 0 or y <0:
			continue
		d += (x - y) ** 2
	return  1/math.sqrt((d+1))

print similarity(list1,list2)
print '\n'
print similarity(list1,list3)
print '\n'
print similarity(list1,list4)
print '\n'
print similarity(list1,list5)


