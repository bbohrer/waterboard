import parser
import os
from flask import *

@app.route('/')
def index():
  (keys, dict) = parser.parse("tests/15150.wat")
  if "Course Info" in keys:
    f = open("html/courseinfo.html", 'r+')
    f.write(makehome(keys, dict["Course Info"]))


if __name__ == '__main__':
  app.run()
  
def makehome(myparts, mydic):
  return render_template("templates/home.html", parts = myparts, dict = mydic)


(keys, dict) = parser.parse("tests/15150.wat")
if "Course Info" in keys:
  f = open("html/courseinfo.html", 'r+')
  f.write(makehome(keys, dict["Course Info"]))

