from flask import Flask, redirect, abort

app = Flask(__name__)

@app.route('/hello')
def hello():
	return "Hello World"

@app.route('/permanent')
def change():
	return redirect("https://mmls.mmu.edu.my/", 302)

@app.route('/change')
def direct():
	return redirect("http://flask.pocoo.org/", 303)

@app.route('/bad_access')
def request():
	abort(400)

@app.route('/authenticate')
def unauthorized():
	abort(401)

@app.route('/forbidden')
def forbid():
	abort(403)

@app.route('/crash')
def server():
	10/0

if __name__ == "__main__":
	app.run(debug = True)