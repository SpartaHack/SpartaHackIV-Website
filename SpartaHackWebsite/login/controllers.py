from flask import Blueprint
from flask import Flask, request, render_template, redirect,session
import re
import requests
import json
from flask import current_app as app

login = Blueprint('login', __name__,template_folder='templates')

def check_creds(email,password):
	url = "https://api.elephant.spartahack.com/sessions"

	headers = {
    'content-type': "application/json",
    'authorization': app.config['API_KEY'],
    #'accept': "vnd.example.v2"			#not sure how this is required
    }
	payload=json.dumps(dict([("email",email),("password",password)]))
	response = requests.request("POST", url,data=payload, headers=headers)
	temp=json.loads(response.text)
	if "errors" in temp:
		return False,temp["errors"]
	else:
		return True,temp

@login.route('/',methods=['GET'])
def loginUser():		#template that log's user in

	if session.get('auth_token') is not None:
		return redirect('/dashboard')

	if request.cookies.get("no_email_error") and request.cookies.get("password_error"):
		return render_template("login.html",email_error=request.cookies.get("no_email_error"),password_error=request.cookies.get("password_error"))

	if request.cookies.get("email_error") and request.cookies.get("password_error"):
		return render_template("login.html",email_error=request.cookies.get("email_error"),password_error=request.cookies.get("password_error"))

	if request.cookies.get("no_email_error"):
		return render_template("login.html",no_email_error=request.cookies.get("no_email_error"))

	if request.cookies.get("email_error"):
		return render_template("login.html",email_error=request.cookies.get("email_error"))

	if request.cookies.get("password_error"):
		return render_template("login.html",password_error=request.cookies.get("password_error"))

	if request.cookies.get("cred_error"):
		return render_template("login.html",cred_error=request.cookies.get("cred_error"))

	return render_template("login.html")


@login.route('/validateLogIn',methods=['POST','GET'])
def validateLogIn():		#did  not create a separate blueprint because user can login from the index page
	#TODO: complete data verfication and set cookies. Talk to API to create a session. Check if user is admin. If yes then reddirect to admin panel

	valid_input=True
	email=request.form['email']
	password=request.form['password']

	response=redirect('/login')
	if not email:
		valid_input=False
		response.set_cookie("no_email_error","Email is required")
	else:
		response.set_cookie("no_email_error",expires=0)  #deleting cookie



	if re.match("^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$", email) != None:
		valid_input=True
		response.set_cookie("email_error",expires=0)
	else:
		response.set_cookie("email_error","That's not an valid email.")
		valid_input=False

	if not password:
		response.set_cookie("password_error","Password is required")
		valid_input=False
	else:
		response.set_cookie("password_error",expires=0)


	if valid_input:
		response.set_cookie("email_error",expires=0)
		response.set_cookie("no_email_error",expires=0)
		response.set_cookie("password_error",expires=0)
		valid,resp=check_creds(email,password)

		if valid:
			response.set_cookie("email_error",expires=0)		#deleting the cookies
			response.set_cookie("password_error",expires=0)
			response.set_cookie("cred_error",expires=0)
			response.set_cookie("no_email_error",expires=0)

			session['username']=resp['first_name']		#setting session data for user
			session['email']=resp['email']
			session['auth_token']=resp['auth_token']
			session['reset_password_token']=resp['reset_password_token']
			session['roles']=resp['roles']
			session['application']=resp['application']
			session['rsvp']=resp['rsvp']
			session['logged_in']=True

			if 'admin' in session['roles']:	#if user logged in as admin redirecting to admin panel
				response=redirect("/admin")
			else:
				response=redirect("/dashboard")

			return response
		else:
			response.set_cookie("cred_error","Invalid Email or Password")
			return response
	else:
		return response
