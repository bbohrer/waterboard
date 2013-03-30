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
if 'DATABASE_URL' in os.environ:
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

def regenerate_website(keys, dict):
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
    if "Announcements" in keys:
      b = open("static/announcements.html", "w+")
      b.write(makeannouncements(keys, dict["Course Info"], dict["Announcements"]))
    if "Staff" in keys:
      b = open("static/staff.html", "w+")
      b.write(makestaff(keys, dict["Course Info"], dict["Staff"]))

@app.before_first_request
def regenerate_website_from_file():
    (keys, dict) = parser.parse("tests/15150.wat")
    regenerate_webite(keys, dict)


@app.route('/admin/', methods=['GET', 'POST'])
def admin():
  #if not session.get('logged_in'):
  if False:
    flash('You have to log in to do that.')
    return redirect(url_for('login'))

  if request.method == 'POST':
    #user = User(request.form['username'], request.form['password'])
    #db.session.add(user)
    #db.session.commit()
    (keys, dict) = parser.parseText(request.form['data'])
    regenerate_website(keys,dict)

    myConfig = open('tests/15150.wat', "w+")
    myConfig.write(request.form['data'])

    b = open("static/events.html", "w+")
    b.write(makeevents(keys, dict["Course Info"]))
    b = open("static/caljavascript.js", "w+")
    b.write(makecalscript(calendardata(keys,dict)))
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
  return app.send_static_file('announcements.html')

@app.route('/staff/')
def staff():
  return app.send_static_file('staff.html')

@app.route('/events/')
def events():
  return app.send_static_file('events.html')

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
  
def makestaff(myheaders, mydic, mycont):
  return render_template('staff.html', headers=myheaders, dict=mydic, cont=mycont)

def makeevents(myheaders, mydic):
  return render_template('events.html', headers=myheaders, dict=mydic)

def calendardata(keys, dict):
  events = []
  if ("Homework" in keys):
    for i,hw in enumerate(dict["Homework"]):
      outdate = datetime.datetime.strptime(hw[0], "%m/%d/%Y")
      duedate = datetime.datetime.strptime(hw[1], "%m/%d/%Y")
      outevent = ("Homework " + str(i + 1) + " released")
      dueevent = ("Homework " + str(i + 1) + " due")
      fileloc = "/homework/" + hw[2]
      events.append((outdate, None, outevent, fileloc))
      events.append((duedate, None, dueevent, fileloc))
  if ("Exams" in keys):
    for i,ex in enumerate(dict["Exams"]):
      date = datetime.datetime.strptime(ex[0], "%m/%d/%Y")
      event = ("Exam " + str(i + 1))
      fileloc = "/exams/" + ex[1]
      events.append((date, None, event, fileloc))
  if ("Lectures" in keys):
    for i,lect in enumerate(dict["Lectures"]):
      date = datetime.datetime.strptime(lect[0], "%m/%d/%Y")
      event = ("Lecture " + str(i + 1))
      fileloc = "/exams/" + lect[1]
      events.append((date, None, event, fileloc))
  if ("Events" in keys):
    for i,even in enumerate(dict["Events"]):
      date = datetime.datetime.strptime(even[0], "%m/%d/%Y")
      event = even[1]
      fileloc = ""
      events.append((date, None, event, fileloc))

  events.append((datetime.datetime.strptime(dict["Course Info"]["cstart"], "%m/%d/%Y")
                , None, "Course Start", ""))
  events.append((datetime.datetime.strptime(dict["Course Info"]["cend"], "%m/%d/%Y")
                , None, "Course End", ""))

  if("Staff" in keys):
      for i,ta in enumerate(dict["Staff"]):
          name = ta["name"]
          for e in ta["events"]:
              tok = e.split(":")
              thing = tok[0].strip()
              when = tok[1].strip()
              whens = when.split(" ")
              strWday = whens[0]
              start = whens[1]
              start_hr = start[:2]
              start_min = start[2:]
              end = whens[2]
              end_hr = end[:2]
              end_min = end[2:]
              wday = ["M","T","W","R","F","Sa","Su"].index(strWday)


              cstart = datetime.datetime.strptime(dict["Course Info"]["cstart"], "%m/%d/%Y")
              cend = datetime.datetime.strptime(dict["Course Info"]["cend"], "%m/%d/%Y")

              cstart2 = cstart.replace(day=(cstart.day + (wday - cstart.weekday())))
              if(cstart2 < cstart):
                cstart2 = cstart2  + timedelta(days=7)

              while cstart2 <= cend:
                  evStart = cstart2.replace(hour= int(start_hr), minute=int(start_min))
                  evEnd = cstart2.replace(hour=int(end_hr), minute=int(end_min))
                  events.append((evStart, evEnd, name + "'s " + thing, ""))
                  cstart2 = cstart2 + datetime.timedelta(days=7)
  return events


def calform(event):
  mystr = ""
  date = str(event[0].date().month) + "/" + str(event[0].date().day)
  if (event[1] == None):
    name = event[2]
    if (event[3] == ""):
      mystr = '{"date":"' + date + '","title":"' + name + '"}'
    else:
      mystr = '{"date":"' + date + '","title":"' + "<a class='callink' href='" + event[3] + "'>" + name + "</a>" + '"}'  
  else: 
    t = str(event[0].time().hour) + ":" + str(event[0].time().minute)+ " - " + str(event[1].time().hour) + ":" + str(event[1].time().minute)
    mystr = '{"date":"' + date + '","title":"' + event[2] + "  " + t + '"}'
  return mystr
    
def makecalscript(allevents):
    strings = [calform(event) for event in allevents]
    return render_template('caljavascript.js', evlist = strings)
      

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    #regenerate_website()
    app.run(host='0.0.0.0', port=port, debug = True) 
