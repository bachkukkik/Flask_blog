from flask import Flask, render_template, url_for
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)