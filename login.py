import flask


app = flask.Flask(__name__)

@app.route('/')
def index():
	return flask.render_template('in.html')

@app.route('/link')
def function():
	return flask.render_template('out.html')

if __name__ == '__main__':
	app.run(debug=True)

