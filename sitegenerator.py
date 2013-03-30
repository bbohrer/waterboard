import parser
import os
from flask import *

app = Flask(__name__)

@app.route('/')
def index():
  (keys, dict) = parser.parse("tests/15150.wat")
  print keys
  if "Course Info" in keys:
    f = open("html/courseinfo.html", 'r+')
    f.write(makehome(keys, dict["Course Info"]))
  return makehome(keys, dict["Course Info"])

def makehome(myheaders, mydic):
  return render_template('home.html', headers = myheaders, dict = mydic)

if __name__ == '__main__':
  app.run(debug=True)
