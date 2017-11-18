from flask import Blueprint
from flask import Flask, request, render_template, redirect, session
import requests

dashboard = Blueprint('dashboard', __name__,template_folder='templates')

def check_password(curr_password,new_password,conf_password):
	url = "https://api.elephant.spartahack.com/users/change_password"

	payload=json.dumps(dict([("current_password",curr_password),("password",new_password),("password_confirmation",conf_password)]))
	headers = {
		'content-type': "application/json",
		'x-www-user-token': session['auth_token']
    }
	response = requests.request("POST", url, data=payload, headers=headers)
	temp=json.loads(response.text)
	if "errors" in temp:
		return False,temp["errors"]
	else:
		return True,temp
	
@dashboard.route('/')
def index():
	if session.get('auth_token') is None:		#if user not logged in then redirect to login page
		return redirect('/login')
	return render_template("dashboard.html")

@dashboard.route('/changepassword')
def changepassword():
	if session.get('auth_token') is None:		#if user not logged in then redirect to login page
		return redirect('/login')
	return render_template("changepassword.html")


@dashboard.route('/changepassword/validatepassword',methods=['POST'])
def validatepassword():
	if session.get('auth_token') is None:		#if user not logged in then redirect to login page
		return redirect('/login')
	curr_password=request.form['currentpassword']
	new_password=request.form['newpassword']
	conf_password=request.form['confpassword']

	if new_password is None or conf_password is None"
		response=redirect("/dashboard/changepassword")
		response.set_cookie("no_pass_change","Password fields cannot be empty")
		return response
	else:
		if new_password!=conf_password:
			response=redirect("/dashboard/changepassword")
			response.set_cookie("pass_change_error","Passwords cannot be diffrent")
			return response
	valid,resp=check_password(curr_password,new_password,conf_password)
	if valid:
		response=redirect('/dashboard')

	return "validate password"
