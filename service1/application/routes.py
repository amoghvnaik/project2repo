from flask import render_template, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from application import app, db, bcrypt, login_manager
from application.models import Users, Proverbs
from application.forms import LoginForm, RegisterForm, UpdateAccountForm, GenerateForm
import requests

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user=Users.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next')

            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))

    return render_template('login.html', title='Log In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data)
        user = Users(email=form.email.data, 
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

login_manager.init_app(app)
@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.delete.data:
            user_id = Users.query.filter_by(id=current_user.id).first()
            db.session.delete(user_id)
            review_id = Reviews.query.filter_by(user_id=None)
            for deleted in review_id:
                db.session.delete(deleted)
            db.session.commit()
            return redirect (url_for('home'))
        elif form.update.data:
            current_user.first_name = form.first_name.data
            current_user.last_name = form.last_name.data
            current_user.email = form.email.data
            db.session.commit()
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
    return render_template('account.html', title='Account', form=form)

@app.route('/generate', methods=['GET', 'POST'])
@login_required
def generate():
    form=GenerateForm()
    if form.submit.data:
        res = requests.get("http://service4:5003").json()["proverb"]
        duplicate = Proverbs.query.filter_by(proverb=res).filter_by(user_id=current_user.id).first()
        if duplicate:
            pass
        else:
            postData = Proverbs(
            proverb=res,
            user=current_user
        )

            db.session.add(postData)
            db.session.commit()
        return render_template ('generate.html', title='Generate Proverb', res=res, form=form)
    return render_template ('generate.html', title='Generate Proverb', form=form)

@app.route('/myproverbs')
@login_required
def myproverbs():
    postData = Proverbs.query.filter_by(user_id=current_user.id).all()
    return render_template('myproverbs.html', title='My Proverbs', proverbs = postData)
