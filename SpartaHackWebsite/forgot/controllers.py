from flask import Blueprint
from flask import Flask, request, render_template

forgot = Blueprint('forgot', __name__,template_folder='templates')


@forgot.route('/')
def index():
    if request.cookies.get("link_sent")=="True":
        link_sent="Password reset link has been sent to:"+"<b>"+resquest.cookies.get(password_reset_email+"</b>")
        return render_template("forgot.html",link_sent=link_sent)
    if request.cookies.get("link_sent")=="False":
        link_not_sent="No account with email:"+"<b>"+resquest.cookies.get(password_reset_email+"</b>"
        return render_template("forgot.html",link_not_sent=link_not_sent)
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
