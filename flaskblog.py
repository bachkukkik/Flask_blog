from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET__KEY'] = '0ebec1a366b4371a8567cff2fc3a2772'

posts = [
    {
        'author': 'Kukkik',
        'title': 'Blog post1',
        'content': 'First Post Content',
        'date_posted': 'April 19, 2020'
    },
    {
        'author': 'bach',
        'title': 'Blog post2',
        'content': 'Second Post Content',
        'date_posted': 'April 20, 2020'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='about')

@app.route("/register")
def register():
	form = RegistrationForm()
	return render_template('register.html', title='Register', form=form)
	
@app.route("/login")
def register():
	form = LoginForm()
	return render_template('login.html', title='Register', form=form)

if __name__ == '__main__':
    app.run(debug=True)
