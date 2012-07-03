from flask_app import app
from flask import render_template, request
from models import Voter, db

@app.route("/")
def voter_list():
    voters = Voter.select().paginate(1, 100).execute()
    return render_template('voter_list.all.html', voters=voters.iterator())

@app.route("/detail/<int:voterid>")
def voter_detail(voterid):
    try:
        voter = Voter.get(id=voterid)
    except Voter.DoesNotExist:
        voter = None
    return render_template('voter_detail.html', voter=voter)

@app.route("/precinct/<int:precinct>")
def voters_by_precinct(precinct):
    voters = Voter.select().where(registeredprecinct=precinct).paginate(1, 100).execute()
    context = {
        'voters': voters.iterator(),
        'precinct': precinct,
    }
    return render_template('voter_list.precinct.html', **context)

@app.route("/search/")
def search():
    query = request.args.get('q')
    field = request.args.get('type', 'name')
    voters = Voter.search(query, field)
    context = {
        'voters': list(voters.iterator())[:100],
        'query': query,
    }
    return render_template('voter_list.search.html', **context)

if __name__ == "__main__":
    app.run(debug=True)
