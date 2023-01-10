from flask import Flask,render_template
#from flask import Flask, redirect, render_template, request, url_for
#from flask_sqlalchemy import SQLAlchemy

# A simple Flask App which takes
# a user's name as input and responds
# with "Hello {name}!"

app = Flask(__name__)
app.config["DEBUG"] = True

#SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
#    username="srmmsu",
#    password="Dev@ng123",
#    hostname="srmmsu.mysql.pythonanywhere-services.com",
#    databasename="srmmsu$comments",
#)
#app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
#app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#db = SQLAlchemy(app)

#@app.route("/")
#def index():
#    return render_template("main_page.html")

comments = []
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template("main_page.html",comments = comments)
    comments.append(request.form["contents"])
    return redirect(url_for('index'))


#@app.route('/', methods=['GET', 'POST'])
#def index():
#    message = ''
#    if flask.request.method == 'POST':
#        message = 'Hello ' + flask.request.form['name-input'] + '!'
#    return flask.render_template('index.html', message=message)

if __name__ == '__main__':
    app.run()
