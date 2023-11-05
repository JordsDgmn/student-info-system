from flask import Blueprint, render_template, request, jsonify, redirect, url_for

index_route = Blueprint('routes', __name__)

@index_route.route("/")
def index():
    return render_template("index.html")
        