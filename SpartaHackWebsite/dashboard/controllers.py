from flask import Blueprint
from flask import Flask, request, render_template, redirect, session

dashboard = Blueprint('dashboard', __name__,template_folder='templates')


@dashboard.route('/')
def index():		
	if session.get('auth_token') is None:		#if user not logged in then redirect to login page
		return redirect('/login')
	return render_template("dashboard.html")

	