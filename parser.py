import yaml,re

def linkify(s):
  return re.sub(r'\[(.*)\]\((.*)\)',r'<a href="\2">\1</a>',s)

def parseCourseInfo(data):
  lines = data['text'].split("\n")
  is_bullet = False
  lines_out = []

  for i in xrange(len(lines)):
    line = lines[i].strip()
    if(0 == line.find("bullet:")):
      rest = line[7:]
      if(not is_bullet):
        lines_out += ["<ul>"]
      is_bullet = True
      lines_out += ["<li>" + rest + "</li>"]
    else:
      if is_bullet:
        lines_out += ["</ul>"]
      is_bullet = False
      if line[:5] == 'head:':
        lines_out += [re.sub(r'^head:(.*)$',r'<h3>\1</h3>',line)]
      else:
        lines_out += ["<p>" + line + "</p>"]
      
  data['text'] = "".join(lines_out)
  data['text'] = linkify(data['text'])
  data['text'] = re.sub(r'^head:(.*)$',r'<h3>\1</h3>',data['text'])
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
  data = map(lambda x: (x['date'],x['text'],x['topic']) , data)
  return data

def parseExams(data):
  for i,a in enumerate(data):
    a['text'] = linkify(a['text'])
    data[i] = a
  data = map(lambda x: (x['date'],x['text'],x['location']) , data)
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

def parseStaff(data):
  return data

def parseText(source):
  data = yaml.load(source)
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
  if "Staff" in data:
    headers.append("Staff")
    ret["Staff"] = parseStaff(data["Staff"])
  return headers,ret

def parse(filename):
  f = open(filename) 
  return parseText(f)

