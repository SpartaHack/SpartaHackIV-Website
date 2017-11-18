from flask import Blueprint
from flask import Flask, request, render_template, redirect,session

logout = Blueprint('logout', __name__,template_folder='templates')


@logout.route('/')
def index():		#using the logout as a blueprint so that user can logout from any page
	
	session.clear()		#user logged out so delete the session data
	return	redirect('/')
	
