from flask_app import app
from forms import Search

@app.context_processor
def inject_search_form():
    return dict(form=Search())
