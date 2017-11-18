from flask import Blueprint
from flask import Flask, request, render_template

forgot = Blueprint('forgot', __name__,template_folder='templates')


@forgot.route('/')
def index():
    return render_template("index.html")