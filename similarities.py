import math

#Test 5 dimension lists
list1 = [5,1,2,6,2]
list2 = [1,3,5,0,3]
list3 = [5,1,2,6,2]
list4 = [99,99,99,99,99]
list5 = [5,-1,-2,-4,2]

data = [list1, list2, list3, list4, list5]

def similarity(a,b):
	distance = 0
	zipped = zip(a,b)

	for x, y in zipped:
		if x < 0 or y < 0:
			continue
		distance += (x - y) ** 2
	return  1 / math.sqrt((distance+1))

def check(input):
    i = 0
    j = 0
    ans = 0
    for person in data:
        j += 1
        if similarity(person, input) > ans:
            ans = similarity(person, input)
            i = j

    print "the best list is list" + str(i) + " with similarity " + str(ans)
    return i

check([5,1,2,6,2])

check([90,90,90,90,90])

#print similarity(list1,list2)
#print '\n'
#print similarity(list1,list3)
#print '\n'
#print similarity(list1,list4)
#print '\n'
#print similarity(list1,list5)


