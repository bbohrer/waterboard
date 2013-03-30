import yaml,re

def linkify(s):
  return re.sub(r'\[(.*)\]\((.*)\)',r'<a href="\2">\1</a>',s)

def parseCourseInfo(data):
  data = linkify(data)
  data = re.sub(r'^head:(.*)$',r'<h4>\1</h4>',data)
  return data

def parseHomework(data):
  for i,a in enumerate(data):
    a['text'] = linkify(a['text'])
    data[i] = a
  data = map(lambda x: (x['out'],x['due'],x['text']) , data)
  return data

def parseLectures(data):
  for i,a in enumerate(data):
    a['text'] = linkify(a['text'])
    data[i] = a
  data = map(lambda x: (x['date'],x['text']) , data)
  return data

def parseAnnouncements(data):
  for i,a in enumerate(data):
    a = linkify(a)
    data[i] = a
  return data

def parseEvents(data):
  for i,a in enumerate(data):
    a['text'] = linkify(a['text'])
    data[i] = a
  data = map(lambda x: (x['date'],x['text']) , data)
  return data

def parse(filename):
  f = open(filename)
  data = yaml.load(f)
  courseinfo = parseCourseInfo(data["Course Info"])
  homework = parseHomework(data["Homework"])
  lectures = parseLectures(data["Lectures"])
  announcements = parseAnnouncements(data["Announcements"])
  events = parseEvents(data["Events"])
