from flask import Flask, render_template, request

from similarities import similarity, check, query

app = Flask(__name__)

@app.route('/')
def default():
    return render_template("intro.html")

@app.route('/home')
def home():
	return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/results',methods=["post"])
def results():
    a = [-1,-1,-1,-1,-1]
    a[0] = int(request.form['rating1'])
    a[1] = int(request.form['rating2'])
    a[2] = int(request.form['rating3'])
    a[3] = int(request.form['rating4'])
    a[4] = int(request.form['rating5'])

    ans = query(a,5)

    return render_template("results.html",query=5,ans=ans)

if __name__=="__main__":
	app.debug = True
	app.run(host="0.0.0.0",port=5000)
