from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash

from .forms import *


#@app.route("/", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def user_options():
    
    form = UserOptionForm()
    if request.method == 'POST' and form.validate_on_submit():
        option = request.form['option']

        if option == "1":
            return redirect('/admin')
        else:
            return redirect("/reservations")
    
    return render_template("options.html", form=form, template="form-template")

@app.route("/admin", methods=['GET', 'POST'])
def admin():

    form = AdminLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = request.form['username']
        password = request.form['password']
        f = open("passcodes.txt",'r')
        for item in f:
            x = item.split(',')
            if username == x[0].strip() and password == x[1].strip():
                return render_template("adminopen.html", form=form, template="form-template")
    return render_template("admin.html", form=form, template="form-template")

@app.route("/reservations", methods=['GET', 'POST'])
def reservations():

    form = ReservationForm()
    if request.method == 'POST' and form.validate_on_submit():
        first_name = request.form['first_name']
        row = request.form['row']
        seat = request.form['seat']
        x = 15
        y = ''.join(random.choices(string.ascii_uppercase + string.digits, k = x))
        f = open('reservations.txt','a')
        f.write(first_name+','+row+','+seat+','+y+'\n')
        f.close()
        return render_template("reservations.html", form=form, template="form-template",message = 'Reservation succesfful, your code is: '+ y)
    return render_template("reservations.html", form=form, template="form-template")

@app.route("/adminopen", methods=['GET', 'POST'])
def adminopen():
    """
    form = AdminLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        first_name = request.form['first_name']
        row = request.form['row']
        seat = request.form['seat']
        x = 15
        y = ''.join(random.choices(string.ascii_uppercase + string.digits, k = x))
        f = open('reservations.txt','a')
        f.write(first_name+','+row+','+seat+','+y+'\n')
        f.close()
        """
    return render_template("adminopen.html",template="form-template")

