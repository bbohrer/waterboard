import yaml,re

def parseCourseInfo(data):
  data = re.sub(r'\[(.*)\]\((.*)\)',r'<a href="\2">\1</a>',data)
  data = re.sub(r'^head:(.*)$',r'<h4>\1</h4>',data)
  return data

def parseHomework(data):
  pass

def parseLectures(data):
  pass

def parseAnnouncements(data):
  pass

def parseEvents(data):
  pass

def parse(filename):
  f = open(filename)
  data = yaml.load(f)
  print data
  courseinfo = parseCourseInfo(data["Course Info"])


parse("tests/15150.wat")
