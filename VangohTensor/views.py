from flask import Flask, request, redirect, url_for, render_template
import requests
from VangohTensor import app
from user import User
from auth import Auth

@app.route('/login')
def login():
    cookie = request.cookies.get('Token')
    if cookie is not None:
        return redirect("/home")
    return render_template('login.html')

@app.route('/logout')
def logout():
    response = redirect("/login")
    response.delete_cookie('Token')
    return response

@app.route('/oauth')
def getToken():
    code = request.args.get('code')
    error = request.args.get('error')
    if error is None:
        error_code = request.args.get('error_code')
        error_description = request.args.get('error_description')
        return redirect(url_for(
            login,
            error=error,
            error_code=error_code,
            error_description=error_description
        ))

    token = Auth(code)
    response = redirect("/home")
    response.set_cookie('Token', token.req())
    return response

@app.route('/home')
def getImages():
    cookie = request.cookies.get('Token')
    # check for non-login users
    if cookie is None:
        return redirect("/login")

    user = User(cookie)

    resp = user.getTop()
    user_full_name = user.getUsername()
    json_data = resp['data']

    return render_template('home.html', json_data=json_data, username=user_full_name)

