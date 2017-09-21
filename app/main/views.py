from flask import Flask, render_template, request, url_for, current_app, redirect, flash, jsonify
from flask_mail import Message
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