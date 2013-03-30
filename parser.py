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

def parseExams(data):
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
  headers = []
  ret = {}
  if "Course Info" in data:
    headers.append("Course Info")
    ret['Course Info'] = parseCourseInfo(data["Course Info"])
  if "Homework" in data:
    headers.append("Homework")
    ret["Homework"] = parseHomework(data["Homework"])
  if "Lectures" in data:
    headers.append("Lectures")
    ret["Lectures"] = parseLectures(data["Lectures"])
  if "Exams" in data:
    headers.append("Exams")
    ret["Exams"] = parseExams(data["Exams"])
  if "Announcements" in data:
    headers.append("Announcements")
    ret["Announcements"] = parseAnnouncements(data["Announcements"])
  if "Events" in data:
    headers.append("Events")
    ret["Events"] = parseEvents(data["Events"])
  return headers,ret
