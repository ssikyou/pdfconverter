import os
from flask import Flask, render_template, request, url_for, current_app, redirect, flash, jsonify
from flask_mail import Message
from werkzeug.utils import secure_filename
from .. import mail
from . import main


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/about")
def about():
    return render_template("about.html")


@main.route("/contact")
def contact():
    return render_template("contact.html")
    

@main.route('/upload', methods = ['GET', 'POST'])
def upload():
   if request.method == 'POST':
      f = request.files['file']
      filename = secure_filename(f.filename)
      f.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
      return 'file uploaded successfully'