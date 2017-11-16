from flask import Blueprint
from flask import Flask, request, render_template
import requests
import json
import operator
main = Blueprint('main', __name__,template_folder='templates')


def get_faqs():
	url = "https://api.elephant.spartahack.com/faqs/"

	headers = {
		'content-type': "application/json",
		'x-www-user-token': "UZb6Ryd2NYgPVXnT_xHL"
		}
	faqs=[]
	response = requests.request("GET", url, headers=headers)
	temp=json.loads(response.text)
	for item in temp:
		if item['placement']=="home" and item['display']==True:
			temp=(item.get('question'),item.get('answer'),item.get('priority'))
			faqs.append(temp)
	faqs.sort(key=operator.itemgetter(2))
	return faqs

	
def get_sponsors():
	url = "https://api.elephant.spartahack.com/sponsors/"
	
@main.route('/')
def index():
	logged_in=None
	faqs=get_faqs()
	sponsors=get_sponsors()
	return render_template("index.html",faqs=faqs,logged_in=logged_in	)