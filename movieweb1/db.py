from pymongo import Connection

c = Connection()
db = c.zzz
users = db.users


def getUsers():
    res = users.find({},{'_id':False})
    return [x for x in res]

def changepassword(email,password):
    res = users.update({'email':email},
                       {'$set':{'password':password}})
    return None

def deleteuser(email):
    res = users.remove({'email':email})
    return None


def addUser(email,password):
    res = users.find({'email':email})
    if res.count()>0:
        return None
    d={}
    result = users.insert({'email':email,'password':password, 'movies':d}) 
    return {'email':email,'password':password}


def checkCredentials(email,password):
    res=users.find({"email":email,"password":password})
    return res.count()==1

def addMovie(email, title):
	movies = users.find({"email":email})[0]["movies"]
	movies[title] = -1
	res = users.update({'email': email}, 
						{'$set':{'movies':movies}})
	return None

def getMovies(email):
	person = users.find({"email":email})[0]
	return str(person["movies"])

# show loop over finding all users
print "HELLO"
if __name__=="__main__":
    pass
