from flask import Blueprint, render_template, request, url_for, redirect, flash, session, send_from_directory
# from main.models import Users, Customers, Employees, Tasks
from wtforms import ValidationError
import re
from datetime import datetime
from flask_login import login_user, login_required, logout_user, current_user
# from main.forms import Loginform, RegistrationForm, CustomersForm, EmployeeForm, TasksForm, HomeSubmit
# from main.extentions import db, login_manager
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms_sqlalchemy.fields import QuerySelectField

auth = Blueprint('auth', __name__, static_folder="main/templates/static")


@auth.route('/')
def index():
    return render_template('Infrastructure.html')
