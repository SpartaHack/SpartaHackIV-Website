from flask import Blueprint
from flask import Flask, request, render_template

forgot = Blueprint('forgot', __name__,template_folder='templates')


@forgot.route('/')
def index():
    if respo
    return render_template("forgot.html")

@forgot.route("/emailsubmit")
def emailsubmit():
    email=request.form['passwordchangeemail']
    if valid:
        reponse=redirect('/forgot')
        response.set_cookie("link_sent","True")
        response.set_cookie("password_reset_email",email)
        return response
    else:
        reponse=redirect('/forgot')
        response.set_cookie("link_sent","False")
        response.set_cookie("password_reset_email",email)
        return response
