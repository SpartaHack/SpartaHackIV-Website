from flask import Blueprint
from flask import Flask, request, render_template

admin = Blueprint('admin', __name__,template_folder='templates')


@admin.route('/')
def index():
    return render_template("admin.html")