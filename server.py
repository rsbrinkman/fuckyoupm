from flask import Flask, render_template, Response
from flask import request
import db

app = Flask(__name__)

@app.route("/")
def index():
    users = db.get_users()
    vote_list = []
    for user in users:
        votes = {}
        votes['user'] = user
        votes['votes'] = db.get_votes(user)
        vote_list.append(votes)
    sorted_list = sorted(vote_list, key=lambda k: k['votes'])
    sorted_list.reverse()

    return render_template('index.html', votes=sorted_list)

@app.route("/test")
def test():
    return db.test()

@app.route('/idiot', methods=['GET'])
def render_idiot():
    return render_template('user.html')

@app.route('/add_idiot', methods=['POST'])
def add_user():
    if request.method == 'POST':
        user = request.form['user']
        db.add_user(user)
    return Response(status=200)


@app.route("/vote", methods=['POST'])
def vote():
    if request.method == 'POST':
        vote = request.form['vote']
        user = request.form['user']
        db.set_vote(vote, user)

    return Response(status=200)

if __name__ == "__main__":
    app.run(debug=True)
