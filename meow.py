from flask import Flask
from icalendar import Calendar, Event
from datetime import date, datetime
import pytz


import parser

app = Flask(__name__)

def makeCal(headers, d):
    cal = Calendar()
    cal.add('prodid', '-//Dick Cheney Software, Inc.//Waterboard//EN')
    cal.add('version', '2.0')

    course = d["Course Info"]["course"]

    for ex in d["Exams"]:
        event = Event()
        for i in xrange(len(ex)):
            my_date = ex[0]
            text = ex[1]
        dates = my_date.split('/')
        event.add('summary', text)
        event.add('dtstamp', datetime(int(dates[2]), int(dates[0]), int(dates[1]),
                                  0,0,0,tzinfo=pytz.utc))
        event.add('dtstart', datetime(int(dates[2]), int(dates[0]), int(dates[1]),
                                  0,0,0,tzinfo=pytz.utc))
        event.add('dtend', datetime(int(dates[2]), int(dates[0]), int(dates[1]),
                                    0,0,0,tzinfo=pytz.utc))
        cal.add_component(event)

    i_lect = 1
    for ex in d["Lectures"]:
        event = Event()
        for i in xrange(len(ex)):
            my_date = ex[0]
            text = ex[1]
        dates = my_date.split('/')
        event.add('summary', str(course) + " Lecture " + str(i_lect))
        i_lect = i_lect + 1
        event.add('dtstamp', datetime(int(dates[2]), int(dates[0]), int(dates[1]),
                                  0,0,0,tzinfo=pytz.utc))
        event.add('dtstart', datetime(int(dates[2]), int(dates[0]), int(dates[1]),
                                  0,0,0,tzinfo=pytz.utc))
        event.add('dtend', datetime(int(dates[2]), int(dates[0]), int(dates[1]),
                                    0,0,0,tzinfo=pytz.utc))
        cal.add_component(event)

    for ex in d["Events"]:
        event = Event()
        for i in xrange(len(ex)):
            my_date = ex[0]
            text = ex[1]
        dates = my_date.split('/')
        event.add('summary', text)
        event.add('dtstamp', datetime(int(dates[2]), int(dates[0]), int(dates[1]),
                                  0,0,0,tzinfo=pytz.utc))
        event.add('dtstart', datetime(int(dates[2]), int(dates[0]), int(dates[1]),
                                  0,0,0,tzinfo=pytz.utc))
        event.add('dtend', datetime(int(dates[2]), int(dates[0]), int(dates[1]),
                                    0,0,0,tzinfo=pytz.utc))
        cal.add_component(event)

    i_hw = 1
    for ex in d["Homework"]:
        event = Event()
        for i in xrange(len(ex)):
            out = ex[0]
            due = ex[1]
            text = ex[2]
        out_dates = out.split('/')
        due_dates = due.split('/')
        event.add('summary', str(course) + " Homework " + str(i_hw))
        i_hw = i_hw + 1
        event.add('dtstamp', datetime(int(out_dates[2]), int(out_dates[0]), int(out_dates[1]),
                                  0,0,0,tzinfo=pytz.utc))
        event.add('dtstart', datetime(int(out_dates[2]), int(out_dates[0]), int(out_dates[1]),
                                  0,0,0,tzinfo=pytz.utc))
        event.add('dtend', datetime(int(due_dates[2]), int(due_dates[0]), int(due_dates[1]),
                                    0,0,0,tzinfo=pytz.utc))
        cal.add_component(event)

    return cal.to_ical()

@app.route("/")
def hello():
    headers,d = parser.parse("tests/15150.wat")
    return makeCal(headers,d)

if __name__ == "__main__":
    app.run(debug=True)
