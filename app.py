from flask import Flask, render_template

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')

@app.route('/')
def index():
	return render_template('pages/home.html')

@app.route('/git')
def git_route():
	return render_template('pages/git.html')

@app.route('/docker')
def docker_route():
	return render_template('pages/docker.html')

if __name__ == '__main__':
    app.run(debug=True)