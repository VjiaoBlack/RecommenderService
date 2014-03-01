import math

#Test lists 5 dimension
list1 = [5,1,2,6,2]
list2 = [1,3,5,0,3]
list3 = [5,1,2,6,2]


def similarity(a,b):

    zipped = zip(a,b)

    for pair in zipped:	
		d = math.sqrt(pair[0] ** 2 + pair[1] ** 2)
		likeness += 1/(d+1)

    return likeness

print similarity(list1,list2)
print '\n'
print similarity(list1,list3)


