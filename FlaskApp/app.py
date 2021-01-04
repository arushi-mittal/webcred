from flask import Flask, redirect, url_for, render_template, request, flash
from flask_dance.contrib.google import make_google_blueprint, google
from flask_dance.contrib.github import make_github_blueprint, github
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter
from pymongo import MongoClient
from forms import PreferencesForm

client = MongoClient('localhost', 27017)
db = client.webcred


app = Flask(__name__)
app.secret_key = "SECRET_KEY"
githubblueprint = make_github_blueprint(
    client_id="Iv1.f76ed7785f89ebc0",
    client_secret="7ade669b113e5b42ea0991e6521b2596136d04e8",
    # redirect_url="/select",
)
app.register_blueprint(githubblueprint, url_prefix="/githublogin")

twitterblueprint = make_twitter_blueprint(
    api_key="rUZEpa7ed83NxKPWgcqkXapaO",
    api_secret="mJ7scHpuSLTtYN2kR5PFseh72a2lxvBJDX1OHI3DxaC6iNr7nL",
    # redirect_url="/select",
)
app.register_blueprint(twitterblueprint, url_prefix="/twitterlogin")

blueprint = make_google_blueprint(
    client_id="588932866512-8quol08hpjvrvsugaoptmcffhgbr4m4o.apps.googleusercontent.com",
    client_secret="-NXgBsmZazQFWLRYPZsnJ4Oq",
    # redirect_url="/select",
    scope=[
        "https://www.googleapis.com/auth/plus.me",
        "https://www.googleapis.com/auth/userinfo.email",
    ]
)
app.register_blueprint(blueprint, url_prefix="/login")
login = ""

@app.route('/')
def home () :
    return render_template('base.html')

@app.route('/showgoogle', methods = ['POST', 'GET'])
def showgoogle ():
    if not google.authorized:
        return redirect(url_for("google.login"))
    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    global login 
    login = resp.json()["email"]
    return redirect(url_for('pref'))

@app.route('/showgithub', methods = ['POST', 'GET'])
def showgithub ():
    if not github.authorized:
        return redirect(url_for("github.login"))
    resp = github.get("/user")
    assert resp.ok
    global login
    login = resp.json()['login']
    logininfo = {"user-login":login,
                "login-mode": "GitHub",
                "sf":0.3,
                "cf":0.4,
                "of":0.3}
    db.User.insert_one(logininfo)
    # return render_template('pref.html', login=login)
    return redirect(url_for('pref'))

@app.route('/showtwitter', methods = ['POST', 'GET'])
def showtwitter ():
    if not twitter.authorized:
        return redirect(url_for('twitter.login'))
    resp = twitter.get("account/settings.json")
    assert resp.ok
    global login
    login = resp.json()['screen_name']
    logininfo = {"user-login":login,
                "login-mode": "Twitter",
                "sf":0.3,
                "cf":0.4,
                "of":0.3}
    db.User.insert_one(logininfo)
    # return render_template('pref.html', login=login)
    return redirect(url_for('pref'))

@app.route('/pref', methods = ['POST', 'GET']) 
def pref () :
    form = PreferencesForm()
    if (request.method == 'POST'):
        if (form.validate() == False):
            flash('Please fill all the weightages correctly')
            return render_template('pref.html', form = form)
        else:
            return render_template('base.html')
    else:
        return render_template('pref.html', form = form)
    return render_template('pref.html')



if __name__ == "__main__":
    app.debug = True
    app.run()