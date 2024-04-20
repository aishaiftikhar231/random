from flask import Blueprint, render_template, request, redirect, url_for, session
@views.route('/')
@views.route('/index')
def index():
    return render_template("index.html")