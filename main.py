from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/mars_explorer.db")


@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    names = dict()
    for job in jobs:
        user = db_sess.query(User).filter(User.id == job.team_leader).first()
        names[job.team_leader] = user.surname + ' ' + user.name
    return render_template("index.html", jobs=jobs, names=names, title="Марсиане")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')