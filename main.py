from flask import Flask, redirect, render_template, request, jsonify, url_for
import pprint
# import Flask from the flask library


# create a flask app like this:
app = Flask(__name__)

# now we need to create our first URL path to trigger the app
# lets make that the home page of our website

@app.route('/') # creates a home page using the route() decorator
def homepage(): # this is triggered when you visit the home page
  return render_template('home.html') # this is what is displayed on the page

@app.route('/home') # specifies the home path
def home(): # triggered when you visit /home
    return redirect(url_for('homepage')) # redirects you to the actual home page

@app.route('/about') # for the about page
def abouts():
    return 'This is the about page'

@app.route('/user/<username>')
def show_profile(username):
  return f'Hello {username}'

@app.route('/server/<int:postID>')
def showServer(postID):
  return f'Server at: {postID}'

@app.route('/chat/<personName>')
def showChat(personName):
  return f'Your chat with {personName}'

@app.route('/contact')
def contact():
  return 'Contact Us at 0412345678'

@app.route('/remind', methods=['POST'])
def remind():
  data = request.get_json()
  pprint.pprint(data)
  return 'yes'

app.run(host='0.0.0.0') # runs the website




