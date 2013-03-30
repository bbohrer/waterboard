import parser
import os
from flask import *
import datetime
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='')
app.secret_key = 'some secret used for cookies'
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
# postgres
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(20))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<Name %r>' % self.username



@app.route('/admin/', methods=['GET', 'POST'])
def admin():
    if not session.get('logged_in'):
        flash('You have to log in to do that.')

        return redirect(url_for('login'))
    
    if request.method == 'POST':
        #user = User(request.form['username'], request.form['password'])
        #db.session.add(user)
        #db.session.commit()
        
        (keys, dict) = parser.parseText(request.form['data'])
        if "Course Info" in keys:
            a = open("static/course info.html", 'w+')
            a.write(makehome(keys, dict["Course Info"]))
        if "Homework" in keys:
            b = open("static/homework.html", 'w+')
            b.write(makehw(keys, dict["Course Info"], dict["Homework"]))
        if "Lectures" in keys:
            b = open("static/lectures.html", 'w+')
            b.write(makehw(keys, dict["Course Info"], dict["Lectures"]))
        if "Exams" in keys:
            b = open("static/exams.html", 'w+')
            b.write(makehw(keys, dict["Course Info"], dict["Exams"]))

        flash('Updated website')

        return redirect(url_for('admin'))

    (keys, mydict) = parser.parse("tests/15150.wat")

    myCurrent = open('tests/15150.wat', 'r').read()

    return render_template('admin.html', headers=keys, dict=mydict["Course Info"], current=myCurrent)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username'] ).first()

        if user == None:
            error = 'Invalid username'
        elif user.password != request.form['password']:
            error = 'Invalid password.' # Should be ' + user.password
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('admin'))

    (keys, mydict) = parser.parse("tests/15150.wat")

    return render_template('login.html', headers=keys, dict=mydict["Course Info"], error=error)

@app.route('/')
@app.route('/course info/')
def course_info():
    return app.send_static_file('course info.html')

@app.route('/homework/')
def homework():
    return app.send_static_file('homework.html')

@app.route('/lectures/')
def lecture():
  return app.send_static_file('lectures.html')
  
@app.route('/exams/')
def exam():
  return app.send_static_file('exams.html')
  
@app.route('/announcements/')
def announcements():
  (keys, dict) = parser.parse("tests/15150.wat")
  return makeannouncements(keys, dict["Course Info"], dict["Announcements"])

def makehome(myheaders, mydic):
  return render_template('home.html', headers = myheaders, dict = mydic)

def makehw(myheaders, mydic, mycont):
  return render_template('homework.html', headers = myheaders, dict = mydic, cont = mycont)
  
def makelect(myheaders, mydic, mycont):
  return render_template('lectures.html', headers = myheaders, dict = mydic, cont = mycont)
  
def makeexam(myheaders, mydic, mycont):
  return render_template('exams.html', headers = myheaders, dict = mydic, cont = mycont)

def makeannouncements(myheaders, mydic, mycont):
  return render_template('announcements.html', headers=myheaders, dict=mydic, cont=mycont)
  
def calendardata(keys, dict):
  events = []
  if ("Homework" in keys):
    for i,hw in enumerate(dict["Homework"]):
      outdate = datetime.strptime(hw[0], "%m/%d/%Y")
      duedate = datetime.strptime(hw[1], "%m/%d/%Y")
      outevent = ("Homework " + str(i + 1) + " released")
      dueevent = ("Homework " + str(i + 1) + " due")
      fileloc = "/homework/" + hw[2]
      events.append(outdate, outevent, fileloc)
      events.append(duedate, dueevent, fileloc)
  if ("Exams" in keys):
    for i,ex in enumerate(dict["Exams"]):
      date = datetime.strptime(ex[0], "%m/%d/%Y")
      event = ("Exam " + str(i + 1))
      fileloc = "/exams/" + ex[1]
      events.append(date, event, fileloc)
  if ("Lectures" in keys):
    for i,lect in enumerate(dict["Lectures"]):
      date = datetime.strptime(lect[0], "%m/%d/%Y")
      event = ("Lecture " + str(i + 1))
      fileloc = "/exams/" + lect[1]
      events.append(date, event, fileloc)
  if ("Events" in keys):
    for i,even in enumerate(dict["Events"]):
      date = datetime.strptime(even[0], "%m/%d/%Y")
      event = even[1]
      fileloc = ""
      events.append(date, event, fileloc)

      
      
      
      
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug = True) 
