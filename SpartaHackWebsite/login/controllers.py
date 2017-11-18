from flask import Blueprint
from flask import Flask, request, render_template, redirect
import re

login = Blueprint('login', __name__,template_folder='templates')


@login.route('/',methods=['GET'])
def loginUser():		#template that log's user in
    return render_template("login.html")
	
@login.route('/validateLogIn',methods=['POST','GET'])
def validateLogIn():		#did  not create a separate blueprint because user can login from the index page
	#TODO: complete data verfication and set cookies. Talk to API to create a session. Check if user is admin. If yes then reddirect to admin panel
	if re.match("^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$", request.form['email']) != None:
		return "Email validated"
		pass
	return redirect('/dashboard')