var ui = {

	// Render the Calendar
	"renderCalendar" : function(mm,yy){
		
		// HTML renderers
		var _html = "";
		var cls = "";
		var msg = "";
		var id = "";
		
		// Create current date object
		var now = new Date();
		
		// Defaults
		if(arguments.length == 0){
			mm = now.getMonth();
			yy = now.getFullYear();
		}
		
		// Create viewed date object
		var mon = new Date(yy,mm,1);
		var yp=mon.getFullYear();
		var yn=mon.getFullYear();
		
		var prv = new Date(yp,mm-1,1);
		var nxt = new Date(yn,mm+1,1);
		
		var m = [
			 "January"
			,"February"
			,"March"
			,"April"
			,"May"
			,"June"
			,"July"
			,"August"
			,"September"
			,"October"
			,"November"
			,"December"
		];
		
		var d = [
			 "Sunday"
			,"Monday"
			,"Tuesday"
			,"Wednesday"
			,"Thursday"
			,"Friday"
			,"Saturday"
		];
		
		// Days in Month
		var n = [
			 31
			,28
			,31
			,30
			,31
			,30
			,31
			,31
			,30
			,31
			,30
			,31
		];
		
		// Events
		var evnt = {"event" : [
			 
       {"date":"12/12","title":"<a class='callink' href='/homework/1.pdf'>Homework 1 released</a>,
         
       {"date":"12/13","title":"<a class='callink' href='/homework/1.pdf'>Homework 1 due</a>,
         
       {"date":"12/14","title":"<a class='callink' href='/homework/2.pdf'>Homework 2 released</a>,
         
       {"date":"12/15","title":"<a class='callink' href='/homework/2.pdf'>Homework 2 due</a>,
         
       {"date":"3/12","title":"<a class='callink' href='/exams/GHC- 4401'>Exam 1</a>,
         
       {"date":"12/13","title":"<a class='callink' href='/exams/GHC- 4401'>Exam 2</a>,
         
       {"date":"1/2","title":"<a class='callink' href='/exams/How to SML'>Lecture 1</a>,
         
       {"date":"2/3","title":"<a class='callink' href='/exams/Type check'>Lecture 2</a>,
         
       {"date":"3/4","title":"<a class='callink' href='/exams/Something else'>Lecture 3</a>,
         
       {"date":"1/2","title":"Monad appreciation day"},
         
       {"date":"1/1","title":"Course Start"},
         
       {"date":"6/1","title":"Course End"},
         
       {"date":"1/2","title":"Brandon Bohrer's Lab  13:30 - 15:0"},
         
       {"date":"1/9","title":"Brandon Bohrer's Lab  13:30 - 15:0"},
         
       {"date":"1/16","title":"Brandon Bohrer's Lab  13:30 - 15:0"},
         
       {"date":"1/23","title":"Brandon Bohrer's Lab  13:30 - 15:0"},
         
       {"date":"1/30","title":"Brandon Bohrer's Lab  13:30 - 15:0"},
         
       {"date":"2/6","title":"Brandon Bohrer's Lab  13:30 - 15:0"},
         
       {"date":"2/13","title":"Brandon Bohrer's Lab  13:30 - 15:0"},
         
       {"date":"2/20","title":"Brandon Bohrer's Lab  13:30 - 15:0"},
         
       {"date":"2/27","title":"Brandon Bohrer's Lab  13:30 - 15:0"},
         
       {"date":"3/6","title":"Brandon Bohrer's Lab  13:30 - 15:0"},
         
       {"date":"3/13","title":"Brandon Bohrer's Lab  13:30 - 15:0"},
         
       {"date":"3/20","title":"Brandon Bohrer's Lab  13:30 - 15:0"},
         
       {"date":"3/27","title":"Brandon Bohrer's Lab  13:30 - 15:0"},
         
       {"date":"4/3","title":"Brandon Bohrer's Lab  13:30 - 15:0"},
         
       {"date":"4/10","title":"Brandon Bohrer's Lab  13:30 - 15:0"},
         
       {"date":"4/17","title":"Brandon Bohrer's Lab  13:30 - 15:0"},
         
       {"date":"4/24","title":"Brandon Bohrer's Lab  13:30 - 15:0"},
         
       {"date":"5/1","title":"Brandon Bohrer's Lab  13:30 - 15:0"},
         
       {"date":"5/8","title":"Brandon Bohrer's Lab  13:30 - 15:0"},
         
       {"date":"5/15","title":"Brandon Bohrer's Lab  13:30 - 15:0"},
         
       {"date":"5/22","title":"Brandon Bohrer's Lab  13:30 - 15:0"},
         
       {"date":"5/29","title":"Brandon Bohrer's Lab  13:30 - 15:0"},
         
       {"date":"1/3","title":"Brandon Bohrer's Lecture  12:0 - 13:30"},
         
       {"date":"1/10","title":"Brandon Bohrer's Lecture  12:0 - 13:30"},
         
       {"date":"1/17","title":"Brandon Bohrer's Lecture  12:0 - 13:30"},
         
       {"date":"1/24","title":"Brandon Bohrer's Lecture  12:0 - 13:30"},
         
       {"date":"1/31","title":"Brandon Bohrer's Lecture  12:0 - 13:30"},
         
       {"date":"2/7","title":"Brandon Bohrer's Lecture  12:0 - 13:30"},
         
       {"date":"2/14","title":"Brandon Bohrer's Lecture  12:0 - 13:30"},
         
       {"date":"2/21","title":"Brandon Bohrer's Lecture  12:0 - 13:30"},
         
       {"date":"2/28","title":"Brandon Bohrer's Lecture  12:0 - 13:30"},
         
       {"date":"3/7","title":"Brandon Bohrer's Lecture  12:0 - 13:30"},
         
       {"date":"3/14","title":"Brandon Bohrer's Lecture  12:0 - 13:30"},
         
       {"date":"3/21","title":"Brandon Bohrer's Lecture  12:0 - 13:30"},
         
       {"date":"3/28","title":"Brandon Bohrer's Lecture  12:0 - 13:30"},
         
       {"date":"4/4","title":"Brandon Bohrer's Lecture  12:0 - 13:30"},
         
       {"date":"4/11","title":"Brandon Bohrer's Lecture  12:0 - 13:30"},
         
       {"date":"4/18","title":"Brandon Bohrer's Lecture  12:0 - 13:30"},
         
       {"date":"4/25","title":"Brandon Bohrer's Lecture  12:0 - 13:30"},
         
       {"date":"5/2","title":"Brandon Bohrer's Lecture  12:0 - 13:30"},
         
       {"date":"5/9","title":"Brandon Bohrer's Lecture  12:0 - 13:30"},
         
       {"date":"5/16","title":"Brandon Bohrer's Lecture  12:0 - 13:30"},
         
       {"date":"5/23","title":"Brandon Bohrer's Lecture  12:0 - 13:30"},
         
       {"date":"5/30","title":"Brandon Bohrer's Lecture  12:0 - 13:30"},
         
		]};
	
		// Leap year
		if(now.getYear()%4 == 0){
			n[1] = 29;
		}
		
		// Get some important days
		var fdom = mon.getDay(); // First day of month
		var mwks = 6 // Weeks in month
		
		// Render Month
		$('.year').html(mon.getFullYear());
		$('.month').html(m[mon.getMonth()]);
		
		// Clear view
		var h = $('#calendar > thead:last');
		var b = $('#calendar > tbody:last');
		
		h.empty();
		b.empty();
		
		// Render Days of Week
		for(var j=0;j<d.length;j++){
			_html += "<th>" +d[j]+ "</th>";
		}
		_html = "<tr>" +_html+ "</tr>";
		h.append(_html);
		
		// Render days
		var dow = 0;
		var first = 0;
		var last = 0;
		for(var i=0;i>=last;i++){
			
			_html = "";
			
			for(var j=0;j<d.length;j++){
				
				cls = "";
				msg = "";
				id = "";
				
				// Determine if we have reached the first of the month
				if(first >= n[mon.getMonth()]){
					dow = 0;
				}else if((dow>0 && first>0) || (j==fdom)){
					dow++;
					first++;
				}
				
				// Format Day of Week with leading zero
				dow = "0" + dow;
				
				// Get last day of month
				if(dow==n[mon.getDate()]){
					last = n[mon.getDate()];
				}
				
				
				// Check Event schedule
				$.each(evnt.event,function(){	
					if(this.date == mon.getMonth()+1 + "/" + dow.substr(-2)){
						cls = "holiday";
						msg = this.title;
					}
				});
				
				
				// Set class
				if(cls.length == 0){
					if(
						dow==now.getDate() 
						&& now.getMonth() == mon.getMonth() 
						&& now.getFullYear() == mon.getFullYear()
					){
						cls = "today";
					}else if(j == 0 || j == 6){
						cls = "weekend";
					}else{
						cls = "";
					}
				}
				
				// Set ID
				id = "cell_" + i + "" + j + "" + dow;
				
				// Render HTML
				if(dow == 0){
					_html += '<td>&nbsp;</td>';
				}else if(msg.length > 0){
					_html += '<td class="' +cls+ '" id="'+id+'">' + dow.substr(-2) + '<br/><span class="content">'+msg+'</span></td>';
				}else{
					_html += '<td class="' +cls+ '" id="'+id+'">' + dow.substr(-2) + '</td>';
				}
				
			}
			
			_html = "<tr>" +_html+ "</tr>";
			b.append(_html);
		}
		
		$('#last').unbind('click').bind('click',function(){
			ui.renderCalendar(prv.getMonth(),prv.getFullYear());
		});
		
		$('#current').unbind('click').bind('click',function(){
			ui.renderCalendar(now.getMonth(),now.getFullYear());
		});
		
		$('#next').unbind('click').bind('click',function(){
			ui.renderCalendar(nxt.getMonth(),nxt.getFullYear());
		});
		
		
	},
	
	
	// Render Clock
	"renderTime" : function(){
		var now = new Date();
		
		var tt = "AM";
		var hh = now.getHours();
		var nn = "0" + now.getMinutes();
		
		if(now.getHours()>12){
			hh = now.getHours()-12;
			tt = "PM";
		}
		
		$('.time').html(
			hh + ":" + nn.substr(-2) + " " + tt
		);
		
		var doit = function(){
			ui.renderTime();
		}
		
		setTimeout(doit,500);
	},
	
	
	// Initialization
	"init" : function(){
	}
	
};


// Initialize
ui.init();


// Load
$(document).ready(function(){
		
	// Render the calendar
	ui.renderCalendar();
	
	ui.renderTime();
	
});