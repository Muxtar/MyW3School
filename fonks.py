from flask import Flask, render_template, redirect, url_for, request, session, make_response
import sys
sys.path.append('__init__')
import sql

class main():
    users = []
    def __init__(self):
        self.app = Flask(__name__)
        self.app.secret_key = 'memo'
        self.inUser = []
        self.statusId = False
        self.errors = {
                "true": True,
                "false": False,
                "sigin" : "Gmail or password error",
                "eynideyil": "Parollar eyni deyil",
                "gmailzanit": "gmail zanit"
                }

        self.error = self.errors['true'] 
        self.loginOrSigin = 'sigin'


    def admin(self):
        self.users = sql.Sql().select()
        self.notReady = sql.Sql(tableName = "notReady").select()
        self.ready = sql.Sql(tableName = "ready").select()
        return render_template("admin.html", users = self.users, notReady = self.notReady, ready = self.ready)

    def delete(self):
        self.id = request.form.get('id')
        sql.Sql().delete('Id', self.id)
        return '0'

    def edit(self):
        self.id = request.form['id']
        self.fname = request.form['fname']
        self.lname = request.form['lname']
        self.gender = request.form['gender']
        self.gmail = request.form['gmail']
        self.password = request.form['password']
        self.status = request.form['userStatus']

        sql.Sql().update(SET = (f"Id = '{self.id}', fName = '{self.fname}', lName = '{self.lname}', gender = '{self.gender}', gmail = '{self.gmail}', password = '{self.password}', status = '{self.status}'"), WHERE = f"Id = '{self.id}'")
        return '0'

    def notReadySend(self):
        self.id = request.form['id']
        self.userId = request.form['userId']
        self.userName = request.form['userName']
        self.title = request.form['title']
        self.thema = request.form['thema']
        self.content = request.form['content']

        sql.Sql(tableName = 'ready').insert(column = "usersId, userName, title, thema, content", value = (self.userId, self.userName, self.title, self.thema, self.content))
        sql.Sql(tableName = 'notReady').delete('id', self.id)
        return '0'

    def notReadyDelete(self):
        self.id = request.form['id']
        sql.Sql(tableName = 'notReady').delete('id', self.id)
        return '0'

    def ready(self):
        return '0'

    def main(self):
        self.setCookies()
        self.loginOrSigin = 'sigin'
        return render_template('main.html')

    def user(self):
        if self.inUser == []:
            self.remember = self.error
            self.error = self.errors['true']
            return render_template('user.html', error = self.remember, loginOrSigin = self.loginOrSigin)

        return redirect(url_for('form'))

    def form(self):
        self.setCookies()
        if self.inUser == []:
            return redirect(url_for('user'))

        self.error = self.errors['true']

        self.content = sql.Sql(tableName = "ready").select()
        self.content.reverse()
        
        return render_template("form.html", content = self.content, user = self.inUser)


    def contents(self, statusId):
        self.setCookies()
        self.statusId = statusId
        self.title = sql.Sql(tableName = 'ready').select(where = f"id = '{self.statusId}'")
        self.contents = sql.Sql(tableName = 'contents').select(where = f"statusId = '{self.statusId}'")
        return render_template("contents.html", titles = self.title, contents = self.contents, userName = self.inUser[0][1])

    # Content iceri yazmaq ucundur
    def yoxla(self):
        self.icerik = request.form.get('icerik')
        sql.Sql(tableName = 'contents').insert(column = 'statusId, userId, userName, userGender, userStatus, content', value = (self.statusId, self.inUser[0][0], self.inUser[0][1], self.inUser[0][4], self.inUser[0][5], self.icerik))
        return 'True'

    def add(self):
        self.fname = request.form['fname']
        self.lname = request.form['lname']
        self.gender = request.form['gender']
        self.gmail = request.form['gmail']
        self.password = request.form['password']
        self.status = request.form['userStatus']

        sql.Sql().insert(column = "fName, lName, gender, gmail, password, status", value = (self.fname, self.lname, self.gender, self.gmail, self.password, self.status))
        userId = sql.Sql().select(select = 'Id', where = f"gmail = '{self.gmail}'")
        return str(userId[0][0])

    def user_sigin(self):
        self.gmail = request.form['gmail']
        self.password = request.form['password']
        
        if (self.gmail, self.password) in sql.Sql().select(select='gmail, password'):
            self.inUser = sql.Sql().select(where = f"gmail = '{self.gmail}' and password = '{self.password}'")

            session['gmail'] = self.gmail            
            session['password'] = self.password

            self.resp = make_response(redirect(url_for('form'), code = 307))
            self.resp.set_cookie('gmail', self.gmail)
            self.resp.set_cookie('password', self.password)

            return self.resp
        
        self.error = self.errors["sigin"]
        self.loginOrSigin = 'sigin'
        return redirect(url_for('user'))

    def user_login(self):
        self.fname = request.form['fname']
        self.lname = request.form['lname']
        self.gmail = request.form['gmail']
        self.gender = request.form['gender']
        self.fpassword = request.form['fpassword']
        self.lpassword = request.form['lpassword']

        self.loginOrSigin = 'login'

        if self.fpassword != self.lpassword:
            self.error = self.errors['eynideyil']
            return redirect(url_for('user'))

        elif (self.gmail,) in sql.Sql().select(select = 'gmail'):
            self.error = self.errors['gmailzanit']
            return redirect(url_for('user'))

        else:
            sql.Sql().insert(column = "fName, lName, gender, gmail, password", value = (self.fname, self.lname, self.gender, self.gmail, self.fpassword))

            self.resp = make_response(redirect(url_for('form')))
            self.resp.set_cookie('gmail', self.gmail)
            self.resp.set_cookie('password', self.fpassword)
            session['gmail'] = self.gmail
            session['password'] = self.fpassword
            self.inUser = sql.Sql().select(where = f"gmail = '{self.gmail}' and password = '{self.fpassword}'")
            return self.resp

    def user_logout(self):
        self.resp = make_response(redirect(url_for('user')))
        self.resp.set_cookie('gmail', '', expires = 0)
        self.resp.set_cookie('password', '', expires = 0)
        session.pop('gmail')
        session.pop('password')
        self.inUser = []
        return self.resp

    def setCookies(self):
        if self.inUser == []:
            self.gmail = request.cookies.get('gmail')
            self.password = request.cookies.get('password')

            if(self.gmail, self.password) in sql.Sql().select(select='gmail, password'):           
                self.inUser = sql.Sql().select(where = f"gmail = '{self.gmail}' and password = '{self.password}'")



    def notready(self):
        self.konu = request.form['konu']
        self.thema = request.form['thema']
        self.icerik = request.form['icerik']

        sql.Sql(tableName = 'notReady').insert(column = "usersId, userName, title, thema, content", value = (self.inUser[0][0], self.inUser[0][1], self.konu, self.thema, self.icerik))

        return redirect(url_for('form'))

    #----

    def test(self, thema, content):
        return render_template(f"{thema}/{content}")

    #----

    def start(self):
        self.app.run(debug = True)
