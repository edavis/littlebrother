from flask import request
from littlebrother import app
from forms import Search
from urllib import urlencode

@app.context_processor
def inject_search_form():
    return dict(form=Search())

@app.context_processor
def inject_get_params():
    params = request.args.copy()
    if 'page' in params:
        del params['page']
    return dict(params=urlencode(params))
