from flask import Blueprint
from flask import Flask, request, render_template,session
import requests
import json
import operator
from flask import current_app as app

main = Blueprint('main', __name__,template_folder='templates')


def get_faqs():
	url = "https://api.elephant.spartahack.com/faqs/"

	headers = {
		'content-type': "application/json",
		'authorisation':app.config['API_KEY']
		}
	faqs=[]
	response = requests.request("GET", url, headers=headers)
	temp=json.loads(response.text)
	for item in temp:
		if item['placement']=="home" and item['display']==True:
			temp=(item.get('question'),item.get('answer'),item.get('priority'))
			faqs.append(temp)
	faqs.sort(key=operator.itemgetter(2))
	temp=None
	return faqs

	
def get_sponsors():

	url = "https://api.elephant.spartahack.com/sponsors/"
	headers = {
	'content-type': "application/json",
	'authorization':app.config['API_KEY']
	}
		
	response = requests.request("GET", url, headers=headers)
	temp=json.loads(response.text)
	trainee_sponsors=[]
	commander_sponsors=[]
	partner_sponsors=[]
	warrior_sponsors=[]
	
	
	for item in temp:
		if item['level'].lower() =="trainee":
			sponsor=(item['url'],item['logo_svg_light'],item['logo_svg_dark'],item['logo_png_dark'])
			trainee_sponsors.append(sponsor)
			
		if item['level'].lower()=="commander":
			sponsor=(item['url'],item['logo_svg_light'],item['logo_svg_dark'],item['logo_png_dark'])
			commander_sponsors.append(sponsor)
			
		if item['level'].lower()=="partner":
			sponsor=(item['url'],item['logo_svg_light'],item['logo_svg_dark'],item['logo_png_dark'])
			partner_sponsors.append(sponsor)

		if item['level'].lower()=="warrior":
			sponsor=(item['url'],item['logo_svg_light'],item['logo_svg_dark'],item['logo_png_dark'])
			warrior_sponsors.append(sponsor)
			
	return (warrior_sponsors,partner_sponsors,commander_sponsors,trainee_sponsors)
	
@main.route('/')
def index():
	if session.get('auth_token') is not None:
		logged_in=True		#for options in nav bar
	else:
		logged_in=False
	faqs=get_faqs()
	warrior_sponsors,partner_sponsors,commander_sponsors,trainee_sponsors=get_sponsors()

	return render_template("index.html",faqs=faqs,logged_in=logged_in,warrior_sponsors=warrior_sponsors,partner_sponsors=partner_sponsors,commander_sponsors=commander_sponsors,trainee_sponsors=trainee_sponsors)