from flask import Blueprint
from flask import Flask, request, render_template, redirect

logout = Blueprint('logout', __name__,template_folder='templates')


@logout.route('/')
def index():		#using the logout as a blueprint so that user can logout from any page
	#TODO: complete cookie distruction and successful session closure
	return	redirect('/')
	
