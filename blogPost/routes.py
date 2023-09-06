from blogPost import app
from flask import render_template, url_for

@app.route('/')
@app.route('/home')
def homepage(): return render_template('home.html')

@app.route('/profile')
def profilepage(): return render_template('profile.html')

@app.route('/createBlog')
def createpage():return render_template('createBlog.html')

@app.route('/viewBlog')
def viewBlogpage(): return render_template('viewBlog.html')


@app.route('/updateBlog')
def profileUpdate(): return render_template('update.html')