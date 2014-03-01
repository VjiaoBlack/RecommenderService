from flask import Flask, render_template, request

from similarities import similarity

app = Flask(__name__)

@app.route('/')
def normal():
	return render_template("home.html")

if __name__=="__main__":
	app.debug = True
	app.run(host="0.0.0.0",port=5000)
