import parser
import os
from flask import *

app = Flask(__name__, static_url_path='')
app.secret_key = 'some secret used for cookies'

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
  
def makehome(myheaders, mydic):
  return render_template('home.html', headers = myheaders, dict = mydic)

def makehw(myheaders, mydic, mycont):
  return render_template('homework.html', headers = myheaders, dict = mydic, cont = mycont)
  
def makelect(myheaders, mydic, mycont):
  return render_template('lectures.html', headers = myheaders, dict = mydic, cont = mycont)
  
def makeexam(myheaders, mydic, mycont):
  return render_template('exams.html', headers = myheaders, dict = mydic, cont = mycont)
  
if __name__ == '__main__':
  app.run(debug=True)
