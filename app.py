from flask import Flask,request,render_template,redirect
from flask_mysqldb import MySQL
app = Flask(__name__)
mysql = MySQL(app)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Rituja@1234'
app.config['MYSQL_DB'] = 'practise'
@app.route('/')
def index():
    return render_template('Form.html')
@app.route("/submit_form",methods=['POST'])
def submit_form():
    FNAME = request.form.get('FNAME')
    LNAME = request.form.get('LNAME')
    email = request.form.get('email')
    password = request.form.get('password')
    DOB = request.form.get('DOB')
    Contact = request.form.get('Contact')
    Document = request.form.get('Document')

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO Candidate_Information_form (FNAME,LNAME,email,password,DOB,Contact,Document) VALUES(%s,%s,%s,%s,%s,%s,%s)",(FNAME,LNAME,email,password,DOB,Contact,Document))
    mysql.connection.commit()
    cur.close()
    return ("Thanks for sharing the detail,Form Submitted Successfully")

if __name__ == '__main__':
    app.run(debug= True,port= 8001)