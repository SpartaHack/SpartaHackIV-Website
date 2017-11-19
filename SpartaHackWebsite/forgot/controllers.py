from flask import Blueprint
from flask import Flask, request, render_template,session,redirect
import requests
import json
from flask import current_app as app

forgot = Blueprint('forgot', __name__,template_folder='templates')


def change_password(newpassword,confpassword,reset_password_token):
    url = "https://api.elephant.spartahack.com/users/reset_password"
    payload=json.dumps(dict([("password",newpassword),("password_confirmation",confpassword)]))
    headers = {
    'content-type': "application/json",
    'x-www-reset-password-token': reset_password_token
    }
    response = requests.request("POST", url, data=payload, headers=headers)

def check_email(email):
    url = "https://api.elephant.spartahack.com/users/request_password_token"
    payload=json.dumps(dict([("email",email)]))
    headers = {
    'content-type': "application/json",
    'authorization': app.config['API_KEY']
    }
    response=requests.request("POST",url,data=payload,headers=headers)
    temp=json.loads(response.text)
    if "errors" in temp:
        return False,temp["errors"]
    else:
        return True,temp

@forgot.route("/passwordreset/validatepass",methods=['POST'])
def validatepass():
    newpassword=request.form['newpassword']
    confpassword=request.form['confpassword']
    reset_password_token=request.form['reset_password_token']
    if newpassword==None or confpassword==None:
        response=redirect('/login')
        response.set_cookie("no_newpassword","Password fields cannot be empty. Request a new link")
        return response
    elif newpassword!=confpassword:
        response=redirect('/login')
        response.set_cookie("newpassword_confpassword _diff","Password fields cannot be diffrent. Request a new link")
        return response
    else:
        change_password(newpassword,confpassword,reset_password_token)
        response=redirect('/login')
        response.set_cookie("no_newpassword",expires=0)
        response.set_cookie("newpassword_confpassword _diff",expires=0)
        response.set_cookie("password_changed","Password changed. Login with the new password")
        return response


@forgot.route("/password/reset/<reset_password_token>")
def password_reset(reset_password_token):
    return render_template("password_reset.html",reset_password_token=reset_password_token)


@forgot.route('/')
def index():
    if request.cookies.get("link_sent")=="True":
        link_sent="Password reset link has been sent to:"+"<b>"+request.cookies.get('password_reset_email')+"</b>"
        #request.set_cookie(link_sent,expires=0)
        return render_template("forgot.html",link_sent=link_sent)
    elif request.cookies.get("link_sent")=="False":
        link_not_sent="No account with email: <b>"+request.cookies.get('password_reset_email')+"</b>"
        #request.set_cookie(link_not_sent,expires=0)
        return render_template("forgot.html",link_not_sent=link_not_sent)
    else:
        return render_template("forgot.html")
@forgot.route("/emailsubmit",methods=['POST'])
def emailsubmit():
    email=request.form['email']
    valid,resp=check_email(email)
    if valid:
        #session['reset_password_token']=resp['reset_password_token']
        response=redirect('/forgot')
        response.set_cookie("link_sent","True")
        response.set_cookie("password_reset_email",email)
        return response
    else:
        response=redirect('/forgot')
        response.set_cookie("link_sent","False")
        response.set_cookie("password_reset_email",email)
        return response
