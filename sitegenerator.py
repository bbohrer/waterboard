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
    b.write(makehw(keys, dict["Course Info"], dict["Homework"]
  return makehome(keys, dict["Course Info"])

def makehome(myheaders, mydic):
  return render_template('home.html', headers = myheaders, dict = mydic)

def makehw(myheaders, mydic, mycont):
  return render_template('homework.html', headers = myheaders, dict = mydic, cont = mycont)
  
if __name__ == '__main__':
  app.run(debug=True)
