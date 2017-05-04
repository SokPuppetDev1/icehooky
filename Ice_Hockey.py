from flask import Flask, render_template
from flask_material import Material 

app = Flask(__name__)
Material(app)

@app.route("/")
def home():
	return render_template('home.html')

@app.route("/History")
def history():
	return render_template('history.html.')

@app.route("/Fixtures")
def fixtures():
	return render_template('fixtures.html')

if __name__=="__main__":
	app.config['DEBUG'] = True
	app.run(host='0.0.0.0')

