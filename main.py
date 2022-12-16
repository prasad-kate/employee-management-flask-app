# Note: External database is used allowing ability to host flask project as this database is used in flask project

from flask import Flask, render_template, request, redirect
import pymysql

app = Flask('__name__')


# Home section ========================================================================================================
@app.route('/')
def home():
    return render_template('home.html')


# Employee details section ===========================================================================================
@app.route('/employee')
def employee():
    try:
        db = pymysql.connect(host='sql6.freesqldatabase.com', user='sql6583839', password='MnUDJbRiRp',
                             database='sql6583839')
        cu = db.cursor()
        q = "select * from employee"
        cu.execute(q)
        data = cu.fetchall()
        return render_template('employee.html', d=data)
    except Exception as e:
        print('Error', e)


# Add Employee details

@app.route('/createEmployee')
def createEmployee():
    return render_template('addEmployee.html')


@app.route('/addEmployee', methods=['POST'])
def addEmployee():
    eid = request.form['eid']
    department = request.form['department']
    fname = request.form['fname']
    lname = request.form['lname']
    dob = request.form['DOB']
    phone = request.form['phone']
    email = request.form['email']
    qualification = request.form['qualification']
    address = request.form['address']
    city = request.form['city']
    postal = request.form['postal']
    doj = request.form['DOJ']
    gender = request.form['gender']
    married = request.form['married']
    try:
        db = pymysql.connect(host='sql6.freesqldatabase.com', user='sql6583839', password='MnUDJbRiRp',
                             database='sql6583839')
        cu = db.cursor()
        q = f"insert into employee values ('{eid}', '{department}', '{fname}', '{lname}', '{dob}', '{phone}', '{email}', '{qualification}', '{address}', '{city}', {postal}, '{doj}', '{gender}', '{married}')"
        cu.execute(q)
        db.commit()
        return redirect('/employee')
    except Exception as e:
        print('Error', e)


# Delete Employee details
@app.route('/deleteEmployee/<rid>')
def deleteEmployee(rid):
    try:
        db = pymysql.connect(host='sql6.freesqldatabase.com', user='sql6583839', password='MnUDJbRiRp',
                             database='sql6583839')
        cu = db.cursor()
        q = f"delete from employee where eid={rid}"
        cu.execute(q)
        db.commit()
        return redirect('/employee')
    except Exception as e:
        print('Error', e)


# Edit Employee Details
@app.route('/editEmployee/<rid>')
def editEmployee(rid):
    try:
        db = pymysql.connect(host='sql6.freesqldatabase.com', user='sql6583839', password='MnUDJbRiRp',
                             database='sql6583839')
        cu = db.cursor()
        q = f"select * from employee where eid = {rid}"
        cu.execute(q)
        data = cu.fetchone()
        return render_template('editEmployee.html', d=data)
    except Exception as e:
        print('Error', e)


# Update Employee Details
@app.route('/updateEmployee/<rid>', methods=['POST'])
def updateEmployee(rid):
    department = request.form['department']
    fname = request.form['fname']
    lname = request.form['lname']
    dob = request.form['birth']
    phone = request.form['phone']
    email = request.form['email']
    qualification = request.form['qualification']
    address = request.form['address']
    city = request.form['city']
    postal = request.form['postal']
    doj = request.form['DOJ']
    gender = request.form['gender']
    married = request.form['married']
    try:
        db = pymysql.connect(host='sql6.freesqldatabase.com', user='sql6583839', password='MnUDJbRiRp',
                             database='sql6583839')
        cu = db.cursor()
        q = f"update employee set department = '{department}', fname = '{fname}', lname = '{lname}', DOB = '{dob}', " \
            f"phone = '{phone}', email = '{email}', qualification = '{qualification}', address = '{address}', " \
            f"city = '{city}', postalCode = '{postal}', DOJ = '{doj}', gender = '{gender}', maritalStatus = '{married}' where eid = {rid}"
        cu.execute(q)
        db.commit()
        return redirect('/employee')
    except Exception as e:
        print('Error', e)


# Emergency contact section  ===========================================================================================
@app.route('/emergency')
def emergency():
    try:
        db = pymysql.connect(host='sql6.freesqldatabase.com', user='sql6583839', password='MnUDJbRiRp',
                             database='sql6583839')
        cu = db.cursor()
        q = "select * from emgcy_contact"
        cu.execute(q)
        data = cu.fetchall()
        return render_template('emergency.html', d=data)
    except Exception as e:
        print('Error', e)


# Add emergency contact
@app.route('/createEContact')
def createEContact():
    return render_template('addEmergency.html')


@app.route('/addEmergency', methods=['POST'])
def addEmergency():
    eid = request.form['eid']
    fname = request.form['fname']
    lname = request.form['lname']
    relation = request.form['relation']
    phone = request.form['phone']
    try:
        db = pymysql.connect(host='sql6.freesqldatabase.com', user='sql6583839', password='MnUDJbRiRp',
                             database='sql6583839')
        cu = db.cursor()
        q = f"insert into emgcy_contact values ('{eid}', '{fname}', '{lname}', '{relation}', '{phone}')"
        cu.execute(q)
        db.commit()
        return redirect('/emergency')
    except Exception as e:
        print('Error', e)


# Delete emergency contact
@app.route('/deleteEmergency/<rid>')
def deleteEmergency(rid):
    try:
        db = pymysql.connect(host='sql6.freesqldatabase.com', user='sql6583839', password='MnUDJbRiRp',
                             database='sql6583839')
        cu = db.cursor()
        q = f"delete from emgcy_contact where eid={rid}"
        cu.execute(q)
        db.commit()
        return redirect('/emergency')
    except Exception as e:
        print('Error', e)


# Edit Emergency contact
@app.route('/editEmergency/<rid>')
def editEmergency(rid):
    try:
        db = pymysql.connect(host='sql6.freesqldatabase.com', user='sql6583839', password='MnUDJbRiRp',
                             database='sql6583839')
        cu = db.cursor()
        q = f"select * from emgcy_contact where eid = {rid}"
        cu.execute(q)
        data = cu.fetchone()
        return render_template('editEmergency.html', d=data)
    except Exception as e:
        print('Error', e)


# Update Emergency Contact
@app.route('/updateEmergency/<rid>', methods=['POST'])
def updateEmergency(rid):
    fname = request.form['fname']
    lname = request.form['lname']
    relation = request.form['relation']
    phone = request.form['phone']
    try:
        db = pymysql.connect(host='sql6.freesqldatabase.com', user='sql6583839', password='MnUDJbRiRp',
                             database='sql6583839')
        cu = db.cursor()
        q = f"update emgcy_contact set fname = '{fname}', lname = '{lname}', relation = '{relation}', phone = '{phone}' where eid = {rid}"
        cu.execute(q)
        db.commit()
        return redirect('/emergency')
    except Exception as e:
        print('Error', e)


# history section  ===========================================================================================
@app.route('/history')
def history():
    try:
        db = pymysql.connect(host='sql6.freesqldatabase.com', user='sql6583839', password='MnUDJbRiRp',
                             database='sql6583839')
        cu = db.cursor()
        q = "select * from history"
        cu.execute(q)
        data = cu.fetchall()
        return render_template('history.html', d=data)
    except Exception as e:
        print('Error', e)


# Add History details
@app.route('/createHistory')
def createHistory():
    return render_template('addHistory.html')


@app.route('/addHistory', methods=['POST'])
def addHistory():
    eid = request.form['eid']
    company = request.form['company']
    address = request.form['address']
    role = request.form['role']
    doj = request.form['DOJ']
    dol = request.form['DOL']
    try:
        db = pymysql.connect(host='sql6.freesqldatabase.com', user='sql6583839', password='MnUDJbRiRp',
                             database='sql6583839')
        cu = db.cursor()
        q = f"insert into history values ('{eid}', '{company}', '{address}', '{role}', '{doj}', '{dol}')"
        cu.execute(q)
        db.commit()
        return redirect('/history')
    except Exception as e:
        print('Error', e)


# Delete history
@app.route('/deleteHistory/<rid>')
def deleteHistory(rid):
    try:
        db = pymysql.connect(host='sql6.freesqldatabase.com', user='sql6583839', password='MnUDJbRiRp',
                             database='sql6583839')
        cu = db.cursor()
        q = f"delete from history where eid={rid}"
        cu.execute(q)
        db.commit()
        return redirect('/history')
    except Exception as e:
        print('Error', e)


# Edit history
@app.route('/editHistory/<rid>')
def editHistory(rid):
    try:
        db = pymysql.connect(host='sql6.freesqldatabase.com', user='sql6583839', password='MnUDJbRiRp',
                             database='sql6583839')
        cu = db.cursor()
        q = f"select * from history where eid = {rid}"
        cu.execute(q)
        data = cu.fetchone()
        return render_template('editHistory.html', d=data)
    except Exception as e:
        print('Error', e)


# Update history
@app.route('/updateHistory/<rid>', methods=['POST'])
def updateHistory(rid):
    company = request.form['company']
    address = request.form['address']
    role = request.form['role']
    doj = request.form['DOJ']
    dol = request.form['DOL']
    try:
        db = pymysql.connect(host='sql6.freesqldatabase.com', user='sql6583839', password='MnUDJbRiRp',
                             database='sql6583839')
        cu = db.cursor()
        q = f"update history set company = '{company}', address = '{address}', role = '{role}', DOJ = '{doj}', DOL = '{dol}' where eid = {rid}"
        cu.execute(q)
        db.commit()
        return redirect('/history')
    except Exception as e:
        print('Error', e)


# leaves section  ===========================================================================================
@app.route('/leaves')
def leaves():
    try:
        db = pymysql.connect(host='sql6.freesqldatabase.com', user='sql6583839', password='MnUDJbRiRp',
                             database='sql6583839')
        cu = db.cursor()
        q = "select * from leaves"
        cu.execute(q)
        data = cu.fetchall()
        return render_template('leaves.html', d=data)
    except Exception as e:
        print('Error', e)


# Add leaves
@app.route('/createLeaves')
def createLeaves():
    return render_template('addLeaves.html')


@app.route('/addLeaves', methods=['POST'])
def addLeaves():
    eid = request.form['eid']
    reason = request.form['reason']
    fd = request.form['from_date']
    td = request.form['to_date']
    try:
        db = pymysql.connect(host='sql6.freesqldatabase.com', user='sql6583839', password='MnUDJbRiRp',
                             database='sql6583839')
        cu = db.cursor()
        q = f"insert into leaves values ('{eid}', '{reason}', '{fd}', '{td}')"
        cu.execute(q)
        db.commit()
        return redirect('/leaves')
    except Exception as e:
        print('Error', e)

# edit leaves
@app.route('/editLeaves/<rid>')
def editLeaves(rid):
    try:
        db = pymysql.connect(host='sql6.freesqldatabase.com', user='sql6583839', password='MnUDJbRiRp',
                             database='sql6583839')
        cu = db.cursor()
        q = f"select * from leaves where eid = {rid}"
        cu.execute(q)
        data = cu.fetchone()
        return render_template('editLeaves.html', d=data)
    except Exception as e:
        print('Error', e)


# Delete leaves
@app.route('/deleteLeaves/<rid>')
def deleteLeaves(rid):
    try:
        db = pymysql.connect(host='sql6.freesqldatabase.com', user='sql6583839', password='MnUDJbRiRp',
                             database='sql6583839')
        cu = db.cursor()
        q = f"delete from leaves where eid={rid}"
        cu.execute(q)
        db.commit()
        return redirect('/leaves')
    except Exception as e:
        print('Error', e)


# update leaves
@app.route('/updateLeaves/<rid>', methods=['POST'])
def updateLeaves(rid):
    reason = request.form['reason']
    from_date = request.form['from_date']
    to_date = request.form['to_date']
    try:
        db = pymysql.connect(host='sql6.freesqldatabase.com', user='sql6583839', password='MnUDJbRiRp',
                             database='sql6583839')
        cu = db.cursor()
        q = f"update leaves set reason = '{reason}', dateFrom = '{from_date}', dateTo = '{to_date}' where eid = {rid}"
        cu.execute(q)
        db.commit()
        return redirect('/leaves')
    except Exception as e:
        print('Error', e)


app.run(debug=True)
