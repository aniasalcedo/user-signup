from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('form.html')


@app.route("/registration", methods=["POST"])
def register():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

# this is for the username error
    if not 20 >= len(username) >= 3 or " " in username:
        username_error = "Error!"

# this is for the password error
    if not 20 >= len(password) >= 3 or " " in password:
        password_error = "Error!"

# this if for the password verify error
    if verify != password:
        verify_error = "Error!"

# this is for email error
    if email != "":
        if not 20 >= len(email) >= 3 or " " in email or email.count("@") >= 1 or email.count(".") >= 1:
            email_error = "Error!"


# this is for all the errors together
    if not username_error and not password_error and not verify_error and not email_error:
        return redirect('/hellomessage?username={0}'.format(username))
    else:
        return render_template('form.html', username=username, username_error=username_error, password=password, password_error=password_error, verify_error=verify_error, email=email, email_error=email_error)


@app.route("/hellomessage")
def valid_signup():
    username = request.args.get('username')
    return render_template('hellomessage.html', username=username)


app.run()
