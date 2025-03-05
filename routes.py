from flask import Blueprint, render_template

# Create a Blueprint
routes_bp = Blueprint("routes", __name__)

@routes_bp.route('/')
def index():
    return render_template('index.html')  # Ensure this file exists in 'templates/'

@routes_bp.route('/')
def login():
    return render_template('login.html')

@routes_bp.route('/')
def register():
    return render_template('register.html')