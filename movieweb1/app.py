from flask import Flask,flash,session,render_template,redirect,request

import db

app=Flask(__name__)

################################################################################
#
#            Replace these routines with your own
#
################################################################################

@app.route("/listsimilar")
def listsimilar():
    return "REPLACE WITH SIMILAR USERS"

@app.route("/recommend")
def recommend():
    return "Replace with recommendations"


################################################################################
#
#     Modify this routine so that it loads the users current movies
#     and also can add a new movie.
#     Remember to change the index.html template to make things look better.
#
################################################################################

@app.route("/",methods=['GET','POST'])
def index():
    if request.method=='GET':
        if 'user' not in session:
            return redirect('/login')

        # query mongo for this users movies
        # and put them in a list of movies and ratings in the form
        # movie[name]=rating
        movies=db.getMovies(session['user'])
        return render_template("index.html",user=session['user'],movies=movies)

    else:
		if 'user' not in session:
			return redirect('/login')

		title=request.form['title']
		check = db.addMovie(session['user'],title)

		if check==None:
			flash("Movie already in list")
		return redirect("/")



################################################################################
#
#    Change this so that it, with the template rate.html makes a form
#    that lets you rate / change your rating for all your movies
#    
#
################################################################################

@app.route("/rate",methods=['GET','POST'])
def rate():
    if request.method=='GET':
        if 'user' not in session:
            return redirect('/login')

        # query mongo for this users movies
        # and put them in a list of movies and ratings in the form
        # movie[name]=rating
        movies={}
        movies['jaws']=3
        movies['star wars']=4
        return render_template("rate.html",user=session['user'],movies=movies)

    # POST code goes here
    button = request.form['button']
    if button=="save":
        # Save the new ratings to mongo
        pass
    
    # Either way, redirect back to the home page
    return redirect("/")

################################################################################
#
#   These routines are good as is.
#   Use them as sample code
#    
#
################################################################################


@app.route("/admin",methods=['get','post'])
def admin():
    if request.method=="GET":
        users = db.getUsers()
        return render_template("admin.html",users=users)

    # deal with changes here
    f =  request.form
    button = f['button']
    if button=="cancel":
        return redirect('/')

    for k in f.keys():
        if k in ['button','password']:
            continue
        (user,action)=k.split(":")
        if action=='change':
            db.changepassword(user,f[user+':password'])
        elif action=="delete":
            db.deleteuser(user)
            
    return redirect('/')


@app.route("/login",methods=["get","post"])
def login():
    if request.method=="GET":
        return render_template("login.html")

    u=request.form['name']
    p=request.form['pass']
    if request.form['button']=='register':
        return redirect("/register")
    
    if db.checkCredentials(u,p):
        session['user']=u
        return redirect("/")
    else:
        flash("INVALID")
        return redirect("/login")

@app.route("/logout")
def logout():
    session.pop('user',None)
    return redirect("/")

@app.route("/register",methods=["get","post"])
def register():
    if request.method=="GET":
        return render_template("register.html")

    u=request.form['name']
    p=request.form['pass']
    if request.form['button']=='cancel':
        return redirect("/")
    check = db.addUser(u,p)
    if check==None:
        flash("username already used")
        return redirect("/register")
    return redirect("/")


if __name__=="__main__":
    app.secret_key="SSSSS"
    app.debug=True
    app.run(host="0.0.0.0",port=4010)
    
