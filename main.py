from flask import Flask, render_template, redirect, url_for, request
app = Flask('app')


@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'magnus' or request.form[
		    'password'] != '1234':
			error = 'Invalid Credentials. Please try again.'

		else:
			return redirect(url_for('admin'))
	return render_template('login.html', error=error)

app.run(host='0.0.0.0', port=8080)