from flask import Flask
from SpartaHackWebsite.main.controllers import main
from SpartaHackWebsite.login.controllers import login
from SpartaHackWebsite.admin.controllers import admin
#from SpartaHackWebsite.live.controllers import live
from SpartaHackWebsite.application.controllers import application
from SpartaHackWebsite.forgot.controllers import forgot
from SpartaHackWebsite.dashboard.controllers import dashboard
from SpartaHackWebsite.logout.controllers import logout
from SpartaHackWebsite.rsvp.controllers import rsvp



app = Flask(__name__)
app.config.from_pyfile("config.cfg")	#set's config rules for the app like base path,secret key etc

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(dashboard, url_prefix='/dashboard')
app.register_blueprint(admin, url_prefix='/admin')
# app.register_blueprint(live, url_prefix='/live')
app.register_blueprint(application, url_prefix='/application')
app.register_blueprint(login, url_prefix='/login')
app.register_blueprint(forgot, url_prefix='/forgot')
app.register_blueprint(logout, url_prefix='/logout')
app.register_blueprint(rsvp, url_prefix='/rsvp')
