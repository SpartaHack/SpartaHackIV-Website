from flask import Blueprint
from flask import Flask, request, render_template, redirect

dashboard = Blueprint('dashboard', __name__,template_folder='templates')


@dashboard.route('/')
def index():
    return render_template("dashboard.html")

	