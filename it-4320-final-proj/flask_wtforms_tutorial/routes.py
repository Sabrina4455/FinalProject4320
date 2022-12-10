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
    #temp is the 2d array storing the seating chart
    #sum1 is storing the total value of all the occupied seats
    form = AdminLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        sum1=0
        cm=get_cost_matrix()
        row=12
        col=4
        temp=[[] for item in range(row)]
        for item in range(row):
            for items in range(col):
                temp[item].append("O")
        temp1=[]
        f=open("reservations.txt",'r')
        for item in f:
            x=item.split()
            y=x[1]
            z=x[2]
            z=int(z.replace(',',""))
            y=int(y.replace(',',""))
            temp2=[y,z]
            temp1.append(temp2)
        for item in temp1:
            temp[item[0]][item[1]]="X"
            sum1=sum1+(cm[item[0]][item[1]])
        username = request.form['username']
        password = request.form['password']
        f = open("passcodes.txt",'r')
        for item in f:
            x = item.split(',')
            if username == x[0].strip() and password == x[1].strip():
                return render_template("admin.html", form=form, template="form-template")
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



def get_cost_matrix():
    cost_matrix = [[100,75,50,100] for row in range(12)]
    return cost_matrix

