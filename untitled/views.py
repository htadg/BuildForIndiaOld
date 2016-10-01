from django.shortcuts import render
from django.http import HttpResponse

from .tasks import T

def run_job():
	T.apply_async(args=("Payment Scheduled",), countdown=3)

def home(request):
	run_job()
	return HttpResponse('<h2>Hope the Task has Started.<h2>')