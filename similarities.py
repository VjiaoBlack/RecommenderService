import math
import db

#Test 5 dimension lists
list1 = [5,1,2,6,2,1]
list2 = [1,3,5,0,3,2]
list3 = [5,1,2,6,2,3]
list4 = [99,99,99,99,99,4]
list5 = [5,-1,-2,-4,2,5]

data = [list1, list2, list3, list4, list5]

def similarity(a,b): # a is a user, b is just a dictionary.
	distance = 0

	zipped = zip(a,b) # ugh, code this function later

	for x, y in zipped:
		if x < 0 or y < 0:
			continue
		distance += (x - y) ** 2
	return  1 / math.sqrt((distance+1))

def check(input): #input is a list of length 'x', represents a user
    i = 0
    j = 0
    ans = 0
    for user in getUsers(): #is getusers right
        j += 1
        if similarity(user, input) > ans:
            ans = similarity(person, input)
            i = j

    print "the best list is list" + str(i) + " with similarity " + str(ans)
    return {
        1:list1,
        2:list2,
        3:list3,
        4:list4,
        5:list5
    }[i]


def query(input,query):
    i = check(input) # i is the list with the best similarity
    return i[query] # returns rating of the query from the one with closest similarity.


# check([5,1,2,6,2])

# check([90,90,90,90,90])

#print similarity(list1,list2)
#print '\n'
#print similarity(list1,list3)
#print '\n'
#print similarity(list1,list4)
#print '\n'
#print similarity(list1,list5)


