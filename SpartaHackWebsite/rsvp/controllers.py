from flask import Blueprint
from flask import Flask, request, render_template,redirect,session

rsvp = Blueprint('rsvp', __name__,template_folder='templates')


@rsvp.route('/')
def index():		#route to rsvp
	#TODO: check for cookies and then proceed to rsvp. If not logged in then redrict to login page
	if session.get('auth_token') is None:		#if user not logged in then redirect to login page
		return redirect('/login')
	if session.get('rsvp'):
		rediret("/dashboard")
	return render_template("rsvp.html")

@rsvp.route('/validatersvp')
def validatersvp():
	attending=request.form['attending']
	foodpref=request.form['foodpref']
	tshirtpref=request.form['tshirtpref']
	jobpref=request.form['jobpref']
