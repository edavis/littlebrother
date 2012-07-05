from littlebrother import app
from flask import render_template, request
from models import Voter
from forms import Search

@app.route("/")
def voter_list():
    return render_template('voter_list.all.html')

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
    search_form = Search(request.args)
    voters = Voter.search(search_form.query.data, search_form.type.data)

    page = int(request.args.get('page', 1))
    voters = voters.paginate(page, app.config['RESULTS_PER_PAGE'])

    context = {
        'voters': voters,
        'form': search_form,
        'next_page_num': page + 1,
    }

    return render_template('voter_list.search.html', **context)

if __name__ == "__main__":
    app.run(debug=True)
