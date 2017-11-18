from flask import Blueprint
from flask import Flask, request, render_template,redirect

rsvp = Blueprint('rsvp', __name__,template_folder='templates')


@rsvp.route('/')
def index():		#route to rsvp
	#TODO: check for cookies and then proceed to rsvp. If not logged in then redrict to login page
	logged_in=None
	return render_template("index.html",logged_in=logged_in)