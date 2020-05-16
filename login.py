from flask import Flask, render_template, redirect, request


app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
	return render_template('in.html')



@app.route('/regi',methods=['GET','POST'])
def regi():
	return render_template('registro.html')



@app.route('/reg',methods=['GET','POST'])
def reg():
	res = ''
	#si el metodo es post se usa request.form['key']
	#si el metodo es get se usa request.args.get('key')
	usuario = request.form['user']
	passw = request.form['passw']
	nomb = request.form['nomb']
	apel = request.form['apel']
	mail = request.form['mail']

	with open('registro.csv', 'a') as f:
		f.writelines('{},{},{},{},{}\n'.format(usuario,passw,nomb,apel,mail))

	with open('registro.csv', 'r') as f:
		ter = f.readlines()
	return render_template('in.html')



@app.route("/link", methods=['POST'])
def rfunction():
	usuario = request.form['user']
	passw = request.form['passw']

	with open('registro.csv', 'r') as f:
		ter = f.readlines()
		for i in ter:
			if (usuario and passw) in i.split(',')[0:2]:
				return render_template('out.html', este=i)
		return render_template('error.html')



if __name__ == '__main__':
	app.run(debug=True)

