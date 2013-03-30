import parser
import os
from flask import *
import datetime

app = Flask(__name__, static_url_path='')
app.secret_key = 'some secret used for cookies'

@app.route('/admin/', methods=['GET', 'POST'])
def admin():
  if False:
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
    if "Announcements" in keys:
      b = open("static/announcements.html", "w+")
      b.write(makeannouncements(keys, dict["Course Info"], dict["Announcements"]))
    if "Staff" in keys:
      b = open("static/staff.html", "w+")
      b.write(makestaff(keys, dict["Course Info"], dict["Staff"]))
    flash('Updated website')
    return redirect(url_for('admin'))

  (keys, mydict) = parser.parse("tests/15150.wat")
  myCurrent = open('tests/15150.wat', 'r').read()
  return render_template('admin.html', headers=keys, dict=mydict["Course Info"], current=myCurrent)

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

def calendardata(keys, dict):
  events = []
  if ("Homework" in keys):
    for i,hw in enumerate(dict["Homework"]):
      outdate = datetime.strptime(hw[0], "%m/%d/%Y")
      duedate = datetime.strptime(hw[1], "%m/%d/%Y")
      outevent = ("Homework " + str(i + 1) + " released")
      dueevent = ("Homework " + str(i + 1) + " due")
      fileloc = "/homework/" + hw[2]
      events.append(outdate, None, outevent, fileloc)
      events.append(duedate, None, dueevent, fileloc)
  if ("Exams" in keys):
    for i,ex in enumerate(dict["Exams"]):
      date = datetime.strptime(ex[0], "%m/%d/%Y")
      event = ("Exam " + str(i + 1))
      fileloc = "/exams/" + ex[1]
      events.append(date, None, event, fileloc)
  if ("Lectures" in keys):
    for i,lect in enumerate(dict["Lectures"]):
      date = datetime.strptime(lect[0], "%m/%d/%Y")
      event = ("Lecture " + str(i + 1))
      fileloc = "/exams/" + lect[1]
      events.append(date, None, event, fileloc)
  if ("Events" in keys):
    for i,even in enumerate(dict["Events"]):
      date = datetime.strptime(even[0], "%m/%d/%Y")
      event = even[1]
      fileloc = ""
      events.append(date, None, event, fileloc)

  events.append(datetime.strptime(dict["Course Info"]["cstart"], "%m/%d/%Y")
                , None, "Course Start", "")
  events.append(datetime.strptime(dict["Course Info"]["cend"], "%m/%d/%Y")
                , None, "Course End", "")

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


              cstart = datetime.strptime(dict["Course Info"]["cstart"], "%m/%d/%Y")
              cend = datetime.strptime(dict["Course Info"]["cend"], "%m/%d/%Y")

              cstart2 = cstart.replace(day=(cstart.day + (wday - day.weekday())))
              if(cstart2 < cstart):
                cstart2 = cstart2  + timedelta(days=7)

              while cstart2 <= cend:
                  evStart = cstart2.replace(hour= start_hr, minute=start_min)
                  evEnd = cstart2.replace(hour=end_hr, minute=end_min)
                  events.append(evStart, evEnd, name + "'s " + thing, "")
                  cstart2 = cstart2 + timedelta(days=7)
  return events

if __name__ == '__main__':
  app.run(debug=True)
