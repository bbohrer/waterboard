import parser
import os
from flask import *

app = Flask(__name__)

@app.route('/')
def index():
  (keys, dict) = parser.parse("tests/15150.wat")
  if "Course Info" in keys:
    a = open("html/courseinfo.html", 'r+')
    a.write(makehome(keys, dict["Course Info"]))
  if "Homework" in keys:
    b = open("html/homework.html", 'r+')
    b.write(makehw(keys, dict["Course Info"], dict["Homework"]))
  return makehome(keys, dict["Course Info"])

@app.route('/course info/')
def course_info():
  (keys, dict) = parser.parse("tests/15150.wat")
  return makehome(keys, dict["Course Info"])

@app.route('/homework/')
def homework():
  (keys, dict) = parser.parse("tests/15150.wat")
  return makehw(keys, dict["Course Info"], dict["Homework"])

def makehome(myheaders, mydic):
  return render_template('home.html', headers = myheaders, dict = mydic)

@app.route('/homework/')
def makehw(myheaders, mydic, mycont):
  return render_template('homework.html', headers = myheaders, dict = mydic, cont = mycont)
  
if __name__ == '__main__':
  app.run(debug=True)
