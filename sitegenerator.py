import parser
import os
from flask import *

app = Flask(__name__, static_url_path='')


@app.route('/admin/', methods=['GET', 'POST'])
def admin():
    #if not session.get('logged_in'):
        #abort(401)

    if request.method == 'POST':
        #user = User(request.form['username'], request.form['password'])
        #db.session.add(user)
        #db.session.commit()
        
        (keys, dict) = parser.parse(request.form['data'])
        if "Course Info" in keys:
            a = open("html/courseinfo.html", 'w+')
            a.write(makehome(keys, dict["Course Info"]))
        if "Homework" in keys:
            b = open("html/homework.html", 'w+')
            b.write(makehw(keys, dict["Course Info"], dict["Homework"]))
        if "Lectures" in keys:
            b = open("html/lectures.html", 'w+')
            b.write(makehw(keys, dict["Course Info"], dict["Lectures"]))
        if "Exams" in keys:
            b = open("html/exams.html", 'w+')
            b.write(makehw(keys, dict["Course Info"], dict["Exams"]))

        flash('Updated website')

        return redirect(url_for('/admin/'))

    (keys, mydict) = parser.parse("tests/15150.wat")

    myCurrent = open('tests/15150.wat', 'r').read()
    print myCurrent

    return render_template('admin.html', headers=keys, dict=mydict["Course Info"], current=myCurrent)

@app.route('/')
@app.route('/course info/')
def course_info():
  (keys, dict) = parser.parse("tests/15150.wat")
  return makehome(keys, dict["Course Info"])

@app.route('/homework/')
def homework():
  (keys, dict) = parser.parse("tests/15150.wat")
  return makehw(keys, dict["Course Info"], dict["Homework"])

@app.route('/lectures/')
def lecture():
  (keys, dict) = parser.parse("tests/15150.wat")
  return makelect(keys, dict["Course Info"], dict["Lectures"])
  
@app.route('/exams/')
def exam():
  (keys, dict) = parser.parse("tests/15150.wat")
  return makeexam(keys, dict["Course Info"], dict["Exams"])
  
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
