from flask import Flask
from models import Voter, db

app = Flask(__name__)

@app.before_request
def before_request():
    db.connect()

@app.teardown_request
def teardown_request(exc):
    db.close()

@app.route("/<voterid>")
def hello(voterid):
    voter = Voter.get(id=voterid)
    return voter.full_name

if __name__ == "__main__":
    app.run(debug=True)
