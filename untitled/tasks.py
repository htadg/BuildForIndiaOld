from __future__ import absolute_import
import urllib2

from celery import task

@task.task(ignore_result=True)
def T(message):
	messagesendurl = "https://control.msg91.com/api/sendhttp.php?authkey=96244AsR6Os06Hs562e546f&mobiles=91"
	messagesendurl += "8447652642"
	messagesendurl += "&message=TEST"
	messagesendurl += "&sender=TEST&route=default&country=0&response=JSON"
	req = urllib2.Request(messagesendurl)
	print urllib2.urlopen(req)
	print "Message :: "+ messagesendurl
	print "Message Sent"