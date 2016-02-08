from flask import render_template, flash, redirect
from app import app
from .forms import MateForm

@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
    form = MateForm()
    if app.matecalypse:
        flash("Ohh noooooooo")
        return render_template("calypse.html",
                               title="Home")
    else:
        if form.validate_on_submit():
            app.matecalypse = True
            return redirect('/')
        return render_template('index.html',
                               title='Home',
                               form=form)
