from flask import Blueprint
from flask import Flask, request, render_template

application = Blueprint('application', __name__,template_folder='templates')


@application.route('/')
def index():
    return render_template("application.html")
	
@application.route('/validateSignUp')
def validateSignUp():
	pass
	
@application.route('/edit')
def edit():
	return render_template("edit.html")
